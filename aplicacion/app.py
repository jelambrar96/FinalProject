import cv2
import numpy as np 
import matplotlib.pyplot as plt

wholes_filenames = [
    'templates/whole/whole_bet.png',
    'templates/whole/whole_over.png'
]

quarters_filenames = [
    'templates/quarter/quarter_bet.png',
    'templates/quarter/quarter_over.png'
]

half_filenames = [
    'templates/half/circle_bet.png',
    'templates/half/circle_over.png'
]

bemol_filenames = [
    'templates/bemol/bemol_bet.png',
    'templates/bemol/bemol_over.png'
]

wholes = [cv2.imread(item, cv2.IMREAD_GRAYSCALE) for item in wholes_filenames]
quartes = [cv2.imread(item, cv2.IMREAD_GRAYSCALE) for item in quarters_filenames]
halfs = [cv2.imread(item, cv2.IMREAD_GRAYSCALE) for item in half_filenames]
bemols = [cv2.imread(item, cv2.IMREAD_GRAYSCALE) for item in bemol_filenames]

symbols = {
    'whole': wholes, 
    'quater': quartes, 
    'half': halfs,
    'bemol': bemols
}


def remove_lines(image):
    pass 

def preprocessing(image):
    pass 

def threshold(img):
    return cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

def adpat_threshold(img):
    return cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)        

def imgerode(image):
    return cv2.erode(image, np.ones((3,3),np.uint8), iterations=1)

def detect_lines(gray):   
    h,w = gray.shape[:2]
    img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,np.pi/180,200)  
    out_lines = []  
    for line in lines:
        for rho,theta in line:
            if np.abs(1.5707963 - theta) < 0.0001 :           
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                #
                x3 = int(x0)
                y3 = int(y0)
                x4 = int(x0 - w*(-b))
                y4 = int(y0 - h*(a))
                #
                cv2.line(img,(x3,y3),(x4,y4),(0,0,255),1)
                out_lines.append([(x3,y3),(x4,y4)])
                #
    return img, out_lines

def sort_y(lines):
    y = [item[0][1] for item in lines]
    y.sort()
    yk = [int(sum(y[i:i+2])/2) for i in range(0, len(y), 2)]
    return [yk[i:i+5] for i in range(0, len(yk), 5)]

def scale(pentalines):
    avg = []
    for item in pentalines:
        dif = [ item[i] - item[i-1] for i in range(1, len(item))]
        avg.append(int(sum(dif)/(len(item)-1)))
    return avg 

def match(image, kernels, th = 0.75, size = 1):
    imgout = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    points = [] 
    for kern in kernels:
        hk, wk = kern.shape[::-1]
        # locations = [] 
        result = cv2.matchTemplate(image, kern, cv2.TM_CCOEFF_NORMED)
        loc = np.where( result >= th)
        pts = zip(*loc[::-1])
        # print(pts)

        """
        plt.figure()
        plt.imshow(result, cmap='gray')
        plt.show()
        """ 

        # points = points + pts
        for item in pts: 
            # print(item)
            points.append(item)
            cv2.rectangle(imgout, item, (item[0] + hk, item[1] + wk), (0,0,255), 2)

    return imgout, points

def detect_symbols(image): 
    cont = 10
    for key, value in symbols.items(): 
    # for key, value in symbols:         
        out, loc = match(image, value, 0.8, 1)
        """
        plt.figure()
        plt.imshow(out)
        plt.show()
        """
        cv2.imwrite('out/' + key + str(cont) + '.png', out)
        cont = cont + 1
