from graphics import *


class Canvas:
    rects = []
    rects_delete = []

    def __init__(self):
        self.win_width = 800
        self.win_height = 600
        self.window = GraphWin("Testing modes", self.win_width, self.win_height, False)

    def draw(self, array):
        self.rects_delete = self.rects
        self.rects = []
        width, height = 30, 30
        start_point = Point(self.win_width / 2 - (width * len(array[0])) / 2, self.win_height / 2 - (height * len(array)) / 2)
        current_point = Point(start_point.x, start_point.y)

        for yItem in array:
            for xItem in yItem:
                if xItem is None:
                    current_point = Point(current_point.x + width, current_point.y)
                    continue
                rect = Rectangle(current_point, Point(current_point.x + width, current_point.y + height))
                rect.setFill(color_rgb(xItem[0], xItem[1], xItem[2]))
                rect.draw(self.window)
                self.rects.append(rect)
                current_point = Point(current_point.x + width, current_point.y)
            current_point = Point(start_point.x, current_point.y + height)
        self.clear_rects()

    def clear_rects(self):
        for item in self.rects_delete[:]:
            item.undraw()
        self.window.update()
