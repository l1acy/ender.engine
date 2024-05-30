![ender.engine](static/banner.png)
<p>
  <img src="https://img.shields.io/badge/powered_by-pygame-green">
  <img src="https://img.shields.io/badge/python-3-yellow">
  <img src="https://img.shields.io/badge/status-indev-lightgray">
</p>

An extension for <a href="https://github.com/pygame/pygame"><img src="https://raw.githubusercontent.com/pygame/pygame/main/docs/reST/_static/pygame_logo.svg" height=16></a>

> [!Warning]
> ender.engine is in development mode

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

Install these libraries before use:
```py
pip install -r requirements.txt
```

Contributors:

<div style="display: flex; gap: 8px; flex-direction: column; justify-content: center">

<table style="border: none">
    <tr>
      <th><a href="https://github.com/stefanlight8"><img src="https://avatars.githubusercontent.com/u/64615032?v=4" width=64 style="border-radius: 100px"></a></th>
      <th><a href="https://github.com/l1acy"><img src="https://avatars.githubusercontent.com/u/101744830?v=4" width=64 style="border-radius: 100px"></a></th>
    </tr>
    <tr>
      <th>stefanlight</th>
      <th>l1acy</th>
    </tr>
</table>

TODO:
- [ ] Make time system
- [ ] Make UI provider