from pygame.event import get as pygameEventGet
from pygame.event import Event as Type

class Events:
    """Class with events"""

    def get() -> list[Type]:
        return pygameEventGet()