import numpy as np
import cv2

# import services.Color as Color
# import services.Canvas as cv
# import time
#
# array = [
#     [None, None, None, None, [0, 0, 0], None, None, None, None],
#     [None, None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None, None],
#     [None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None],
#     [None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None],
#     [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
#     [None, None, None, None, [0, 0, 0], None, None, None, None],
#     [None, None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None, None],
#     [None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None],
#     [None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None],
#     [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
#     [None, None, None, None, [0, 0, 0], None, None, None, None],
#     [None, None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None, None],
#     [None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None],
#     [None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None],
#     [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
# ]

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    img = cv2.resize(img, (340, 220))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([80, 100, 255])
    upperBound = np.array([120, 255, 255])
    mask = cv2.inRange(hsv_frame, lowerBound, upperBound)  # поиск ядовито зеленого цвета.

    # Display the resulting frame
    cv2.imshow('frame', mask)
    points = cv2.findNonZero(mask)
    if points is not None:
        avg = np.mean(points, axis=0)
        print(avg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
