import  cv2
import  os

i =0
video =cv2.VideoCapture("1.mp4")
while video.isOpened():
    _,rasm =video.read()
    path ="Photo"
    cv2.imwrite(os.path.join(path, f'{i} -rasm.jpg'),rasm)
    cv2.imshow("Video",rasm)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i +=1
video.release()
cv2.destroyAllWindows()