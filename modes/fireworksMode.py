import math
import time
import random
import copy


def check_position(position, x, y):
    for row in position:
        for col in row:
            if x == col[0] and y == col[1]:
                return True
    return False


def fireworks_mode(config):
    rocket_color = (0, 0, 0)
    background_color = (0, 150, 30)
    blow_light = (0, 250, 30)
    blow_dark = (0, 200, 30)
    middle_matrix = math.floor(config["matrix_width"] / 2)
    height = config["matrix_height"]
    start_position = [
        [[middle_matrix, height - 3]],
        [[middle_matrix - 1, height - 2], [middle_matrix + 1, height - 2]],
        [[middle_matrix, height - 1]],
    ]
    # letter Ц
    # start_position = [
    #     [[middle_matrix - 2, height - 6], [middle_matrix + 2, height - 6]],
    #     [[middle_matrix - 2, height - 5], [middle_matrix + 2, height - 5]],
    #     [[middle_matrix - 2, height - 4], [middle_matrix + 2, height - 4]],
    #     [[middle_matrix - 2, height - 3], [middle_matrix + 2, height - 3]],
    #     [
    #         [middle_matrix - 2, height - 2],
    #         [middle_matrix - 1, height - 2],
    #         [middle_matrix, height - 2],
    #         [middle_matrix + 1, height - 2],
    #         [middle_matrix + 2, height - 2],
    #         [middle_matrix + 3, height - 2]
    #     ],
    #     [[middle_matrix + 3, height - 1]],
    #     [[middle_matrix + 3, height]],
    # ]
    current_position = copy.deepcopy(start_position)
    is_raining = False
    is_rained = False
    rain_step = 0

    while True:
        array = []
        is_blew = current_position[len(current_position) - 1][0][1] <= -1

        if is_blew:
            if rain_step <= height - 1:
                rain_step += 1
            else:
                rain_step = 0
                is_rained = not is_rained

                if is_rained:
                    is_raining = True

        if not is_rained and is_raining and is_blew:
            is_raining = False
            is_blew = False
            current_position = copy.deepcopy(start_position)

        # drawing
        for y in range(height):
            array.append([])
            for x in range(config["matrix_width"]):
                is_particle = (x % 2 == 0 if y % 2 else x % 2 == 1)
                is_rain = y >= rain_step if is_rained else y <= rain_step

                if is_blew and is_particle and is_rain:
                    array[y].append(blow_light if random.randrange(2) == 1 else blow_dark)
                elif check_position(current_position, x, y):
                    array[y].append(rocket_color)
                else:
                    array[y].append(background_color)

        # move
        for row in current_position:
            for col in row:
                col[1] -= 1 if col[1] >= 0 else 0

        time.sleep(0.1 if is_blew else 0.3)
        yield array
