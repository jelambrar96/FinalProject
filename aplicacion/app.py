import cv2
import numpy as np 
import matplotlib.pyplot as plt

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
    for line in lines:
        for rho,theta in line:
            if np.abs(1.5707963 - theta) < 0.0001 :           
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho

                x3 = int(x0)
                y3 = int(y0)
                x4 = int(x0 - w*(-b))
                y4 = int(y0 - h*(a))

                cv2.line(img,(x3,y3),(x4,y4),(0,0,255),1)

    return img

