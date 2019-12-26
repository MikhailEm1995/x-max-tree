import services.Color as Color
import time


def gradient_mode(config):
    color_from = (0, 255, 30)
    color_to = (0, 80, 20)

    while True:
        array = []
        color_generator = Color.animate_color(color_from, color_to, 18)

        for y in range(config["matrix_height"]):
            current_color = next(color_generator)
            array.append([])
            for x in range(config["matrix_width"]):
                array[y].append(current_color)
        time.sleep(0.1)
        yield array