import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,1)
    # print ret
    cv2.imshow('frame1',gray)
    cv2.imshow('frame2',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()
