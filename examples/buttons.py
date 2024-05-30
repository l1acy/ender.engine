import ee
import ee.draw

router = ee.Router(
    title="My ender.engine window",
    size=ee.RouterSize(500, 500)
)

app = router.build()

buttons = ee.ButtonsGroup([(ee.Button((300, 300), (380, 380)), lambda: print("Button clicked!"))])

buttonsProvider = ee.ButtonsProvider([buttons])

running = True
while running:
    app.fill((255, 255, 255))
    ee.draw.rect(app, (255, 0, 0), (300, 300, 380, 380))

    for event in ee.Events.get():
        if event.type == ee.EventType.quitAction:
            running = False
        if event.type == ee.EventType.mouseDown:
            buttonsProvider.check()

    ee.Router.flip()

quit()