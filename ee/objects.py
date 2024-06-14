from ee.types import Surface

class Objects:
    def __init__(self) -> None:
        self.objects: dict[tuple[Surface]]
        self.objects = []

    def add(self, object: Surface):
        self.objects.append((object, object.get_rect()))

    def render(self, app: Surface):
        for object in self.objects:
            item, rect = object
            app.blit(item, rect)