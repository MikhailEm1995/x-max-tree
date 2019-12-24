import services.Color as Color
import time

# Signature
# def mode(config):
# config.matrix_height = number
# config.matrix_width = number
# config.current_coords = [float, float]
# config.current_color = (number, number, number)
# config.play_sound = def func(local_sound_filename):


def idle(config):
    color_from = (0, 0, 255)
    color_to = (255, 0, 0)
    color_current = Color.animate_color(color_from, color_to, 60)

    while True:
        array = []
        color = next(color_current)

        for y in range(config["matrix_height"]):
            array.append([])
            for x in range(config["matrix_width"]):
                array[y].append(color)
        time.sleep(0.1)
        yield array
