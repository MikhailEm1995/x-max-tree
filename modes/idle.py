import services.Color as Color
import random
import time


# Signature
# def mode(config):
# config.matrix_height = number
# config.matrix_width = number
# config.current_coords = [float, float]
# config.current_color = (number, number, number)
# config.play_sound = def func(local_sound_filename):

def idle(config):
    mode = random_mode(config)

    while True:
        yield next(mode)


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


def random_mode(config):
    while True:
        array = []

        for y in range(config["matrix_height"]):
            array.append([])
            for x in range(config["matrix_width"]):
                color = (random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1))
                array[y].append(color)
        time.sleep(0.1)
        yield array
