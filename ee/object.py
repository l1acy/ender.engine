from ee.types import Surface, Router

from pygame import image, transform

class Object:
    def __init__(
        self,
        texture: str,
        router: Router,
    ) -> None:
        self.texturePath = router.path + texture

        self.texture = image.load(self.texturePath).convert_alpha()
        self.rect = self.texture.get_rect()

    def increase(self, size: int):
        self.texture = transform.scale_by(self.texture, size)

    def resise(self, width: int = 0, height: int = 0):
        if width == 0: width = self.texture.get_width()
        if height == 0: height = self.texture.get_height()

        if width + height == 0: raise ValueError("Width and height cannot be set together at the same time")

        self.texture = transform.scale(self.texture, (width, height))

    def rotate(self, angle: int = 90):
        self.texture = transform.rotate(self.texture, angle)
    
    def flipX(self):
        self.texture = transform.flip(self.texture, True, False)

    def flipY(self):
        self.texture = transform.flip(self.texture, False, True)

    def render(self, app: Surface):
        app.blit(self.texture, self.rect)