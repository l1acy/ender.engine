from ee.types import Surface
from ee.buttons import ButtonProvider

from typing import Callable

import pygame

class Slider:
    def __init__(self, background: Surface, dragger: Surface, root: Surface) -> None:
        self._x = 0
        self._y = 0

        self.background = background
        self.background_rect = self.background.get_rect()

        self.dragger = dragger
        self.dad = self.dragger.get_rect()

        self.dragger_button: ButtonProvider = None

        self.is_follow = False

        self.root = root

        self.percents = 0

        """DragAndDrop"""

    def calculate(self) -> float:
        slider_width = self.background.get_width() - self.dad.width * 0.71
        one_percents = slider_width / 100

        drager_x = self.dad.x - self.background_rect.x

        percents = round(drager_x / one_percents)

        self.percents = percents
        print(percents)
        return percents
    
    def paint(self, x: int, y: int):
        self._x = x
        self._y = y
        if self.dragger_button is None:
            self.dragger_button = ButtonProvider((x, y), (self.background.get_width(), self.background.get_height() + y))
            self.dad.x = x


        background_rect = self.background_rect
        background_rect.y = y
        background_rect.x = x
        self.root.blit(self.background, background_rect)

        dragger_rect = self.dad
        dragger_rect.y = y - self.background.get_height() * 0.4
        self.root.blit(self.dragger, dragger_rect)

        if self.is_follow:
            self.follow_mouse()

    def check(self, action: Callable = None):
        if self.dragger_button.check(action):
            self.is_follow = True
            print("follow activated")

    def follow_mouse(self):
        mousePos = pygame.mouse.get_pos()
        max_x = self.background.get_width() + self.background_rect.x - self.dragger.get_width() / 1.4
        mX, mY, = mousePos
        self.dad.x, self.dad.y = mX - 20, self.dad.y
        if max_x < self.dad.x:
            self.dad.x = max_x
        if self.dad.x < self.background_rect.x:
            self.dad.x = self.background_rect.x

        self.calculate()

    def disable_follow_mouse(self):
        self.is_follow = False