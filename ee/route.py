from dataclasses import dataclass

from pygame import (
    init as app_init,
    display as display,
    Surface,
    RESIZABLE,
    NOFRAME
)

from pygame.time import Clock

@dataclass
class RouterSize:
    width: int = 500
    height: int = 300

class Router():
    def __init__(
        self,
        path: str,
        resousesPath: str,
        title: str = "enger.engine",
        size = RouterSize(),
        resizable: bool = True,
    ):
        self.title = title
        self.size = size

        self.resizeable = resizable

        self.screen: ...

        self.path = path + "\\" + resousesPath + "\\"

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

    def flip():
        display.flip()