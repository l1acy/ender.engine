from pygame import(
    QUIT,
    KEYDOWN,
    KEYUP,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEWHEEL,
    JOYBUTTONDOWN,
)

class EventType:
    keyDown = KEYDOWN
    keyUp = KEYUP
    mouseDown = MOUSEBUTTONDOWN
    mouseUp = MOUSEBUTTONUP
    mouseWheel = MOUSEWHEEL
    quitAction = QUIT
    gamepadPress = JOYBUTTONDOWN