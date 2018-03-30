# https://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/
# https://stackoverflow.com/questions/11676864/how-can-i-format-an-integer-to-a-two-digit-hex
import numpy as np
import cv2
import os
cap = cv2.VideoCapture('output.avi')
count=0
while(cap.isOpened()):
    ret, frame = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #dst_gray = cv2.bilateralFilter(frame,d=8, sigmaColor=60, sigmaSpace=100)
    if (count < 400):
        cv2.imwrite(os.path.join("out_images", "{:04}".format(count)+".png"),frame)
        count+=1
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

