class ModeRunner:
    def __init__(self, generator, renderer):
        self.generate_frame = generator
        self.render = renderer
    
    def take_step(self):
        frame = next(self.generate_frame)

        self.render(frame)
