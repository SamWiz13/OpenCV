import  cv2
import numpy as np

i =0
video =cv2.VideoCapture("1.mp4")
while video.isOpened():
    _,rasm =video.read()
    rasm =np.rot90(rasm,i%4)
    cv2.imshow("Video",rasm)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i +=1
video.release()
cv2.destroyAllWindows()