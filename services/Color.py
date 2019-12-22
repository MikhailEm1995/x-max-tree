import math


def get_delta_color(c_from, c_to, step):
    d_r_col = math.floor(c_from[0] - c_to[0]) if c_from[0] > c_to[0] else math.floor(c_to[0] - c_from[0])
    d_r_col = math.floor(d_r_col / step) if d_r_col != 0 else 0
    d_g_col = math.floor(c_from[1] - c_to[1]) if c_from[1] > c_to[1] else math.floor(c_to[1] - c_from[1])
    d_g_col = math.floor(d_g_col / step) if d_g_col != 0 else 0
    d_b_col = math.floor(c_from[2] - c_to[2]) if c_from[2] > c_to[2] else math.floor(c_to[2] - c_from[2])
    d_b_col = math.floor(d_b_col / step) if d_b_col != 0 else 0

    return d_r_col, d_g_col, d_b_col


def get_correct_chanel(chanel):
    if chanel > 255:
        return 255
    elif chanel < 0:
        return 0
    else:
        return chanel


def get_correct_color(color):
    correct_color = [0, 0, 0]

    i = 0
    while i < len(color):
        correct_color[i] = get_correct_chanel(color[i])
        i += 1

    return correct_color[0], correct_color[1], correct_color[2]


def next_color(c_from, c_to, d_r_col, d_g_col, d_b_col):
    c_r = c_from[0] - d_r_col if c_from[0] > c_to[0] else c_from[0] + d_r_col
    c_g = c_from[1] - d_g_col if c_from[1] > c_to[1] else c_from[1] + d_g_col
    c_b = c_from[2] - d_b_col if c_from[2] > c_to[2] else c_from[2] + d_b_col

    return get_correct_color((c_r, c_g, c_b))


def animate_color(c_from, c_to, step):
    delta_color = get_delta_color(c_from, c_to, step)
    previous_color = next_color(c_from, c_to, delta_color[0], delta_color[1], delta_color[2])

    while True:
        previous_color = next_color(previous_color, c_to, delta_color[0], delta_color[1], delta_color[2])
        print(previous_color)
        yield previous_color
