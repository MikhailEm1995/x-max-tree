import RPi.GPIO as GPIO
import time

class Signals:
    coords = []

    def __init__(self, config):
        self.config = config

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        for key in self.config.modes_buttons_pins:
            GPIO.setup(
                self.config.modes_buttons_pins[key],
                GPIO.IN,
                pull_up_down=GPIO.PUD_DOWN
            )

    def setup_watch_mode_change(self):
        for key in self.config.modes_buttons_pins:
            GPIO.add_event_detect(
                self.config.modes_buttons_pins[key],
                GPIO.RISING,
                callback=self.set_mode_callback(key)
            )

    def set_mode_callback(self, mode):
        def set_mode():
            self.config.current_mode = mode
            GPIO.cleanup()

        return set_mode

    def setup_watch_motion_coords(self):
        # to be implemented
        return None

    