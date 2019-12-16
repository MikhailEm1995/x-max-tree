from neopixel import *

class FrameRenderer:
    def __init__(self, canva, strip):
        self.canva = canva
        self.strip = strip

    def get_frame(self, frame_mtx):
        return [
            [
                [
                    (
                        address,
                        Color(**frame_mtx[row_idx, cell_idx])
                    ) for address in cell
                ] for cell_idx, cell in enumerate(row)
            ] for row_idx, row in enumerate(self.canva)
        ]

    def render(self, frame):
        for row in frame:
            for cell in row:
                for address, color in cell:
                    self.strip.setPixelColor(address, color)
        
        self.strip.show()
