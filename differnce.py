import cv2

img1 = cv2.imread("differnce1.jpg")
img2 = cv2.imread("differnce2.jpg")


resized1= cv2.resize(img1, (450,350))
cv2.waitKey(0)

resized2 = cv2.resize(img2, (450,350))
cv2.waitKey(0)

show = resized2 - resized1
print('\n',show)
show[show<40] = 255
cv2.imshow("Differnce",show)
cv2.waitKey(0)

