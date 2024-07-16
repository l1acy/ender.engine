class Animation:
    def __init__(self, *frames) -> None:
        self.frames = frames
        print(frames)
        self.current = -1
        self.all = len(self.frames) - 1

    def next(self):
        self.current += 1
        if self.current > self.all:
            self.current = 0

        return self.frames[self.current]

    def get(self):
        return self.frames[self.current]