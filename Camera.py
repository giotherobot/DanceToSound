import numpy as np
import cv2
from Buffer import *

def nothing(x):
    pass

cv2.namedWindow('slider')

cap = cv2.VideoCapture(0)

cv2.createTrackbar('a', 'slider', 0, 100, nothing)

B1 = Buffer(50, cap.get(4), cap.get(3))

ret, outFrame = cap.read()

while True:

    ret, inFrame = cap.read()

    B1.addFrame(inFrame)

    frames = B1.getFrames(10, 3)

    a = cv2.getTrackbarPos('a', 'slider')/100

    for i,img in enumerate(frames):
        outFrame = cv2.addWeighted(outFrame, a*i, img, a*i, 0)

    cv2.imshow('frame', outFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
