import services.Canvas as cv
import modes.idle as mode

canvas = cv.Canvas()
idle = mode.idle({"matrix_height": 30, "matrix_width": 30})

while True:
    canvas.draw(next(idle))
