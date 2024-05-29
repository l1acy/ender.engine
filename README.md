![ender.engine](static/banner.png)
<p>
    <img src="https://img.shields.io/badge/powered_by-pygame-green">
    <img src="https://img.shields.io/badge/python-3-yellow">
    <img src="https://img.shields.io/badge/status-indev-lightgray">
</p>

<a href="https://github.com/pygame/pygame/"><img src="https://raw.githubusercontent.com/pygame/pygame/main/docs/reST/_static/pygame_logo.svg" alt="pygame" height=16></a> fork

Use example:
```py
import ee

app = ee.Router(
    title="GitHub Example",
    size=ee.RouterSize(width=500, height=333)
)
screen = app.build()
clocks = ee.Router.clocks(app)

running = True
while running:
    clocks.tick(45)
    screen.fill(color=ee.Colors.white)

    for event in ee.Events.get():
        if event.type == ee.EventType.quitAction:
            running = False

    ee.Router.flip()

quit()
```
