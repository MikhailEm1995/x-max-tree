import services.Color as Color
import time


def flow_mode(config):
    color_current = Color.animate_array_colors([
        (0, 57, 56),  # dark green
        (0, 134, 91),  # light green
        (90, 193, 59),  # green
        (255, 255, 47),  # yellow
        (235, 41, 15),  # red
    ])

    while True:
        array = []
        color = next(color_current)

        for y in range(config["matrix_height"]):
            array.append([])
            for x in range(config["matrix_width"]):
                array[y].append(color)
        time.sleep(0.1)
        yield array
