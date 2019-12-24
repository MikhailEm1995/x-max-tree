import services.Canvas as cv
import modes.idle as mode

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
idle = mode.idle(array)

while True:
    canvas.draw(next(idle))
