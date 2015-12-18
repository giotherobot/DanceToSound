import numpy
import cv2


def nothing(x):
    pass


cap = cv2.VideoCapture(0)
# ret, sfondo = cap.read()

cv2.namedWindow('frame')
cv2.createTrackbar('a', 'frame', 0, 255, nothing)
# cv2.createTrackbar('b', 'frame', 0, 100, nothing)

while True:
    # if cv2.waitKey(1) & 0xFF == ord('a'):
    #     ret, sfondo = cap.read()

    ret, frame = cap.read()

    # sfondoG = cv2.cvtColor(sfondo, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.bitwise_not(frame)

    val1 = cv2.getTrackbarPos('a', 'frame')
    # val2 = cv2.getTrackbarPos('b', 'frame')

    # retval, thresh1 = cv2.threshold(frame, val1, 255, cv2.THRESH_BINARY)
    thresh1 = cv2.adaptiveThreshold(frame, val1, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 4)

    # mask = cv2.bitwise_or(sfondoG,  frameG)

    cv2.imshow('frame', thresh1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

