import  numpy as np
import  matplotlib.pyplot as plt
import  matplotlib.image as mimg
import  cv2

picture =cv2.imread("swordd.jpg")
print(picture.shape)
gray_image =cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')

print(gray_image.shape)
plt.show()
