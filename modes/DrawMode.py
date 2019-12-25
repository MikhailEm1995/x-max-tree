import math
import numpy as np
import cv2

paintColor = (255, 0, 0)

camera = {
    'width': 640,
    'height': 320,
}

array = [
    [None, None, None, None, [0, 0, 0], None, None, None, None],
    [None, None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None, None],
    [None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None],
    [None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [None, None, None, None, [0, 0, 0], None, None, None, None],
    [None, None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None, None],
    [None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None],
    [None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [None, None, None, None, [0, 0, 0], None, None, None, None],
    [None, None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None, None],
    [None, None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None, None],
    [None, [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], None],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
]

arrayWidth = len(array[0])
arrayHeight = len(array)

cap = cv2.VideoCapture(0)

# задаем границы ядовито зеленого цвета.
# Изначально цвет задается в HSV-формате, который маппится по правилам:
# 0º-359º <-> [0-179]
# 0%-100% <-> [0-255]
# последний параметр, value, пробрасывается без маппинга
lowerBound = np.array([80, 100, 255])
upperBound = np.array([120, 255, 255])


def getXs(x):
    return x * arrayWidth / camera['width']


def getYs(y):
    return y * arrayHeight / camera['height']


def getPointInArray(point):
    return math.floor(getXs(point[0])), math.floor(getYs(point[1]))


def setColorInArray(point):
    x = point[0]
    y = point[1]
    if array[y][x] is not None:
        array[y][x] = paintColor
        print(array)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    img = cv2.resize(frame, (camera['width'], camera['height']))
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_frame, lowerBound, upperBound)

    points = cv2.findNonZero(mask)
    if points is not None:
        averagePoint = np.mean(points, axis=0)[0]
        pointInArray = getPointInArray(averagePoint)  # получаем точку в ёлке
        setColorInArray(pointInArray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
