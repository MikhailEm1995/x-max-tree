import services.Canvas as cv
import modes.idle as mode

canvas = cv.Canvas()
idle = mode.idle({"matrix_height": 18, "matrix_width": 26})

while True:
    canvas.draw(next(idle))
