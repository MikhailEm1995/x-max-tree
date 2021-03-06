from modes.fireworksMode import fireworks_mode

# Signature
# def mode(config):
# config.matrix_height = number
# config.matrix_width = number
# config.current_coords = [float, float]
# config.current_color = (number, number, number)
# config.play_sound = def func(local_sound_filename):


def idle(config):
    mode = fireworks_mode(config)

    while True:
        yield next(mode)
