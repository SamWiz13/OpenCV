import cv2


i =0
video =cv2.VideoCapture("1.mp4")
img =cv2.imread("sword.jpg")
while video.isOpened():
    _,rasm =video.read()
    cv2.imshow("Video",rasm)
    if i%12 ==0:
        cv2.imshow("Img",img)
        i +=1
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i +=1
video.release()
cv2.destroyAllWindows()
