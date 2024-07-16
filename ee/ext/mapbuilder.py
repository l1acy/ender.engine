from ee.types import Surface
from ee.draw import rect

from ee import Router

from pygame import image

from pygame import transform


class MapBuilder:
    """
    Text example:
    ```
    height=3
    000
    000
    111
    0=air.png
    1=grass.png
    ```
    """
    def __init__(self, text: str, router: Router, tile_px_size: int) -> None:
        self.text = text

        self.lines = self.text.splitlines()
        self.height = self.lines[0]
        self.data = {}

        self.router = router

        for element in self.lines[1 + int(self.height[7:]):]:
            key, value = element.split("=")

            texture = image.load(self.router.path + value)
            if texture.get_width() != tile_px_size:
                self.size = tile_px_size
                texture = transform.scale_by(texture, tile_px_size / texture.get_width())

            self.data.update({key: texture.convert_alpha()})


    def build(self):
        screen = self.router.screen
        x = 0
        y = 0

        Pxsize = 1.75
        size = self.size

        for i in self.lines[1:int(self.height[7:]) + 1]:
            x = 0
            for block in [*i]:
                screen.blit(self.data[block], (x*size, y*size))
                x += 1
            
            y += 1