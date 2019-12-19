import modes.Canvas as cv
import time

array = [
    [None, None, None, None, (), None, None, None, None],
    [None, None, None, (), (), (), None, None, None],
    [None, None, (), (), (), (), (), None, None],
    [None, (), (), (), (), (), (), (), None],
    [(), (), (), (), (), (), (), (), ()],
    [None, None, None, None, (), None, None, None, None],
    [None, None, None, (), (), (), None, None, None],
    [None, None, (), (), (), (), (), None, None],
    [None, (), (), (), (), (), (), (), None],
    [(), (), (), (), (), (), (), (), ()],
    [None, None, None, None, (), None, None, None, None],
    [None, None, None, (), (), (), None, None, None],
    [None, None, (), (), (), (), (), None, None],
    [None, (), (), (), (), (), (), (), None],
    [(), (), (), (), (), (), (), (), ()],
]

array2 = [
    [None, None, None, None, (), None, None, None, None],
    [None, None, None, (), (), (), None, None, None],
    [None, None, (), (), (), (), (), None, None],
    [None, (), (), (), (), (), (), (), None],
    [(), (), (), (), (), (), (), (), ()],
]

canvas = cv.Canvas()
canvas.draw(array)
time.sleep(1)
canvas.draw(array2)
canvas.window.getMouse()
