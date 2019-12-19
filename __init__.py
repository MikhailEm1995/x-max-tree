import threading
from .AppConfig import AppConfig
from .classes.Signals import Signals
from .classes.ModeRunner import ModeRunner
from .classes.FrameRenderer import FrameRenderer

if __name__ == "__init__":
    strip = Adafruit_NeoPixel(
        AppConfig.strip_pin,
        AppConfig.led_count,
        AppConfig.strip_freq_hz,
        AppConfig.strip_dma,
        AppConfig.strip_invert,
        AppConfig.strip_brightness,
        AppConfig.strip_channel
    )
    strip.begin()

    signals = Signals(AppConfig)
    renderer = FrameRenderer(AppConfig.canvas, strip)
    
    buttons_watcher = threading.Thread(target=signals.setup_watch_mode_change)
    buttons_watcher.start()

    runners = {}

    for key in AppConfig.modes:
        runners[key] = ModeRunner(AppConfig.modes[key], renderer)

    current_runner = runners[AppConfig.current_mode]
    prev_mode = "idle"

    while True:
        if AppConfig.current_mode != prev_mode:
            current_runner = runners[AppConfig.current_mode]
            prev_mode = AppConfig.current_mode
        else:
            current_runner.take_step()
