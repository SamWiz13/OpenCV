import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 =plt.imread('car_green_screen.jpg')
img1 =cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
plt.figure(figsize=(12,3))
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
copy_img =np.copy(img1)
maska =cv2.inRange(copy_img,lower_blue,upper_blue)
plt.subplot(141)
plt.imshow(img1)
plt.subplot(142)
plt.imshow(img1[:,:,0],cmap='gray')
plt.subplot(143)
plt.imshow(img1[:,:,1],cmap='gray')
plt.subplot(144)
plt.imshow(img1[:,:,2],cmap='gray')

plt.show()