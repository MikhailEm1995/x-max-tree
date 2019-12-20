import modes.Canvas as cv
import time

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

canvas = cv.Canvas()
while True:
    for yItem in array:
        for xItem in yItem:
            if xItem is None:
                continue
            xItem[0] += xItem[0] > 250 if 0 else 10
            xItem[1] += xItem[1] > 250 if 0 else 10
            xItem[2] += xItem[2] > 250 if 0 else 10
    canvas.draw(array)
    time.sleep(0.3)
canvas.window.getMouse()
