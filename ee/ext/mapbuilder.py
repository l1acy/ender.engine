from ee.types import Surface
from ee.draw import rect

from ee import Router

from pygame import image


class MapBuilder:
    """
    Text example:
    ```
    height=3
    000
    000
    111
    1=grass.png
    ```
    """
    def __init__(self, text: str) -> None:
        self.text = text

    def build(self, screen: Surface, path: str):

        lines = self.text.splitlines()
        height = lines[0]
        data = {}

        for element in lines[1 + int(height[7:]):]:
            key, value = element.split("=")

            texture = image.load(path + value)

            data.update({key: texture.convert_alpha()})

        x = 0
        y = 0

        Pxsize = 1.75
        size = 50

        for i in lines[1:int(height[7:]) + 1]:
            x = 0
            for block in [*i]:
                if data[block] is tuple:
                    rect(screen, data[block] (x*size, y*size, size, size))
                else:
                    screen.blit(data[block], (x*size, y*size))
                x += 1
            
            y += 1


        Router.flip()