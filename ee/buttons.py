from typing import Callable

from pygame.mouse import get_pos as cursorPosition

from pygame.display import Info as display
# from pygame.display import _VidInfo

from typing import Any


class Button:
    def __init__(
        self,
        coordsA: tuple[int, int],
        coordsB: tuple[int, int]
    ) -> None:
        self.a = coordsA
        self.b = coordsB

class ButtonsGroup:
    """
    A group of buttons that can be turned on or off, for example when opening the inventory

    Arguments:
    - buttons: list[tuple[Button, Function]] #Buttons in group
    - IsDisabled: bool = False # Is this group disabled for default?
    - id: int = 0 # ID of the group, can stay zero. Several groups can have the same ID, it is needed to check groups for different events

    Examples:
    ```py
    group = ee.buttons.ButtonsGroup(
        [
            (ee.buttons.Button((0,0), (120, 50)), lambda: print("Button clicked!"))
        ]
    )
    ```
    or
    ```py
    def printButtonClick():
        print("Button clicked!")

    group = ee.buttons.ButtonsGroup(
        [
            (ee.buttons.Button((0,0), (120, 50)), printButtonClick)
        ]
    )
    ```
    """
    def __init__(
        self,
        buttons: list[tuple[Button, Callable]],
        IsDisabled: bool = False
    ) -> None:
        self.buttons = buttons
        self.IsDisabled = IsDisabled

    def toogle(self):
        if self.IsDisabled:
            self.IsDisabled = False
        else:
            self.IsDisabled = True

    def addButton(self, button: tuple[Button, Callable]):
        if isinstance(button, type(tuple[Button, Callable])):
            raise ValueError("Arg button must be: tuple[Button, Callable] (Callable: function() or lambda)")

        self.buttons.append(button)


    def removeButton(self, index: int):
        if not isinstance(index, int):
            raise ValueError("Arg index must be: int")

        self.buttons.pop(index)

class ButtonsProvider:
    def __init__(
        self,
        buttons: list[ButtonsGroup],
    ) -> None:
        self.buttons = buttons
    
    def check(self) -> None:
        """
        Detect button presses on the screen using a mouse/finger.

        Example:
        ```py
        for event in ee.Events.get():
            if event.type == ee.EventType.mouseDown:
                buttonsProvider.check()
        ```
        """
        for group in self.buttons:
            for button in group.buttons:

                if group.IsDisabled: break

                button, function = button

                xfrom, yfrom = button.a

                xto, yto = button.b

                xto *= 1.75
                yto *= 1.75

                x, y = cursorPosition()


                if x > xfrom and x < xto and y > yfrom and y < yto:
                    function()