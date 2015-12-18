import numpy
import cv2


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
# ret, sfondo = cap.read()

cv2.namedWindow('frame')
cv2.createTrackbar('Blur', 'frame', 1, 50, nothing)
cv2.createTrackbar('Cont', 'frame', 0, 50, nothing)

while True:

    ret, frame = cap.read()

    frameG = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    val1 = cv2.getTrackbarPos('Blur', 'frame')*2 + 1

    frameG = cv2.GaussianBlur(frameG, (val1, val1), 0)

    ret1, thresh1 = cv2.threshold(frameG, 127, 255, 0)

    img, conto, hier = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    val2 = cv2.getTrackbarPos('Cont', 'frame')
    if val2 >= len(conto):
        val2 -= len(conto)

    cv2.drawContours(frameG, conto, val2, (0, 255, 0), 3)
    cv2.imshow('frame', frameG)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

