import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('samples/fire.jpg',0)
img = cv2.medianBlur(img,5)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th2, th3]

for i in range(3):
    plt.figure();plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    plt.show()
