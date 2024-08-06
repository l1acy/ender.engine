from dataclasses import dataclass

from pygame import (
    init as app_init,
    display as display,
    Surface,
    RESIZABLE,
    NOFRAME,
    transform
)

import math

from pygame.time import Clock

@dataclass
class RouterSize:
    width: int = 500
    height: int = 300

class Router():
    def __init__(
        self,
        path: str = "",
        resourses_path: str = "",
        title: str = "enger.engine",
        size = RouterSize(),
        resizable: bool = True,
    ):
        self.title = title
        self.size = size

        self.resizeable = resizable

        self.screen: Surface

        self.path = path + "\\" + resourses_path + "\\"

    def build(self) -> Surface:
        app_init()
        screen = display.set_mode((self.size.width, self.size.height), RESIZABLE)
        display.set_caption(self.title)

        self.screen = screen
        return screen

    def clocks(self):
        return Clock()

    def update():
        display.update()

    def flip(*args):
        display.flip()

    def fill_image(self, image: Surface, scaleBy: float | int = 0):
        image = transform.scale_by(image, scaleBy)
        sizeW = image.get_width()
        sizeH = image.get_height()

        x = 0
        y = 0

        times_x = math.ceil(self.screen.get_width() / sizeW)
        times_y = math.ceil(self.screen.get_height() / sizeH)

        for i in range(times_y):
            x = 0
            for block in range(times_x):
                self.screen.blit(image, (x*sizeW, y*sizeH))
                x += 1
            
            y += 1