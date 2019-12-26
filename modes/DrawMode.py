import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# задаем границы ядовито зеленого цвета.
# Изначально цвет задается в HSV-формате, который маппится по правилам:
# 0º-359º <-> [0-179]
# 0%-100% <-> [0-255]
# последний параметр, value, пробрасывается без маппинга
lowerBound = np.array([80, 100, 255])
upperBound = np.array([120, 255, 255])

def setColorInArray(point, canvas, color):
    x = point[0]
    y = point[1]
    if canvas[y][x] is not None:
        canvas[y][x] = color
    return canvas

def startDrawMode(config, signals):
    camera = config.camera
    canvas = config.canvas
    paint_color = config.current_paint_color

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        img = cv2.resize(frame, (camera['width'], camera['height']))
        hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv_frame, lowerBound, upperBound)

        points = cv2.findNonZero(mask)
        if points is not None:
            averagePoint = np.mean(points, axis=0)[0]
            pointInArray = signals.setup_watch_motion_coords(averagePoint)  # получаем точку в ёлке
            setColorInArray(pointInArray, canvas, paint_color)
            yield canvas

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
