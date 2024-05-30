from .enums.eventType import EventType

class DeviseType:
    keyboard = 0
    gamepad = 1
    phone = 2

class Devises:
    def check(event) -> DeviseType:
        if event.type == EventType.gamepadPress:
            return DeviseType.gamepad
        elif event.type == EventType.keyDown:
            return DeviseType.keyboard