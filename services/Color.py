import math


def get_delta_color(c_from, c_to, step):
    d_r_col = math.ceil(c_from[0] - c_to[0]) if c_from[0] > c_to[0] else math.ceil(c_to[0] - c_from[0])
    d_r_col = math.ceil(d_r_col / step) if d_r_col != 0 else 0
    d_g_col = math.ceil(c_from[1] - c_to[1]) if c_from[1] > c_to[1] else math.ceil(c_to[1] - c_from[1])
    d_g_col = math.ceil(d_g_col / step) if d_g_col != 0 else 0
    d_b_col = math.ceil(c_from[2] - c_to[2]) if c_from[2] > c_to[2] else math.ceil(c_to[2] - c_from[2])
    d_b_col = math.ceil(d_b_col / step) if d_b_col != 0 else 0

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


def get_valid_next_color(value, default_value, direction):
    if direction:
        result = default_value if value > default_value else value
    else:
        result = default_value if value < default_value else value

    return get_correct_chanel(result)


def next_color(c_from, c_to, d_r_col, d_g_col, d_b_col):
    c_r = get_valid_next_color(c_from[0] - d_r_col, c_to[0], False) \
        if c_from[0] > c_to[0] else get_valid_next_color(c_from[0] + d_r_col, c_to[0], True)
    c_g = get_valid_next_color(c_from[1] - d_g_col, c_to[1], False) \
        if c_from[1] > c_to[1] else get_valid_next_color(c_from[1] + d_g_col, c_to[1], True)
    c_b = get_valid_next_color(c_from[2] - d_b_col, c_to[2], False) \
        if c_from[2] > c_to[2] else get_valid_next_color(c_from[2] + d_b_col, c_to[2], True)

    return c_r, c_g, c_b


def animate_color(c_from, c_to, step):
    delta_color = get_delta_color(c_from, c_to, step)
    previous_color = next_color(c_from, c_to, delta_color[0], delta_color[1], delta_color[2])

    while True:
        previous_color = next_color(previous_color, c_to, delta_color[0], delta_color[1], delta_color[2])
        yield previous_color


def animate_array_colors(colors):
    direction = True
    from_index = 0
    end_index = 1

    while True:
        current_generator = animate_color(colors[from_index], colors[end_index], 30)
        current_color = next(current_generator)

        while current_color != colors[end_index]:
            current_color = next(current_generator)
            yield current_color

        if direction:
            from_index += 1
            end_index += 1

            if end_index >= len(colors):
                direction = False
                from_index = end_index - 1
                end_index = from_index - 1
        else:
            from_index -= 1
            end_index -= 1

            if end_index <= 0:
                direction = True
                from_index = 0
                end_index = 1
