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

cv.draw(array)
time.sleep(1)
cv.draw(array2)
