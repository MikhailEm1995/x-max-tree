import services.Color as Color
import time


def idle(array):
    color_from = (0, 0, 255)
    color_to = (255, 0, 0)
    color_current = Color.animate_color(color_from, color_to, 10)

    while True:
        color = next(color_current)

        for yItem in array:
            for xItem in yItem:
                if xItem is None:
                    continue
                xItem[0] = color[0]
                xItem[1] = color[1]
                xItem[2] = color[2]
        time.sleep(0.1)
        yield array
