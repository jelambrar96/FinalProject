import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
import app 

def main():

    path = '/home/jelambrar/Git/FinalProject/aplicacion/demos_musescores/All_Dudes/All_Dudes-001.jpg'
    # path = '/home/jelambrar/Git/SheetVision/resources/samples/sheet.jpg'
    # path = '/home/jelambrar/Git/FinalProject/aplicacion/demos_musescores/Reunion/Reunion-001.jpg'
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image2 = app.threshold(image)
    image3 = app.imgerode(image2)
    out = app.detect_lines(image)
    cv2.imwrite('out/lines.jpg',image2)
    plt.figure()
    plt.imshow(out)


    plt.figure()
    plt.imshow(image3, cmap='gray')


    plt.show() 

if __name__ == '__main__':
    main()    