import services.Canvas as cv
import modes.idle as mode

canvas = cv.Canvas()
idle = mode.idle({"matrix_height": 20, "matrix_width": 27})

while True:
    canvas.draw(next(idle))
