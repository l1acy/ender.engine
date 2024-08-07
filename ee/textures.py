"""router.textures"""
from ee.types import Surface
from pygame import image


class TexturesCloud:
    def __init__(self, directory_path: str, name: str = "ender.engine") -> None:
        self.name = name
        self.direcory = directory_path

        self.textures: dict[str: ...] = {}

    def load(self, data: ..., key: str, file: bool = True) -> None:
        """
        Example
        ```py
        TexturesCloud().load("player.png", file=True, key="game.player")
        ```"""
        if file:
            data = image.load(self.direcory + data)

        self.textures.update({key: data})
    
    def get(self, key: str) -> ...:
        """### Return None if key doesn't exists"""
        return self.textures.get(key, None)