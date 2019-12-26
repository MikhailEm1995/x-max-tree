import time
import random


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