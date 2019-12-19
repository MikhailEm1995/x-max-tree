from graphics import *

def draw(array):
    win_width = 800
    win_height = 600
    window = GraphWin("Testing modes", win_width, win_height)
    width, height = 30, 30
    start_point = Point(win_width / 2 - (width * len(array[0])) / 2, win_height / 2 - (height * len(array)) / 2)
    current_point = Point(start_point.x, start_point.y)

    for yItem in array:
        for xItem in yItem:
            if xItem is None:
                current_point = Point(current_point.x + width, current_point.y)
                continue
            rect = Rectangle(current_point, Point(current_point.x + width, current_point.y + height))
            rect.setFill(color_rgb(30, 30, 30))
            rect.draw(window)
            current_point = Point(current_point.x + width, current_point.y)
        current_point = Point(start_point.x, current_point.y + height)
    window.getMouse()
    window.close()
