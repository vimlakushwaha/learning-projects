from ursina import *            # this will import everything we need from ursina with just one line.

app = Ursina()
ground = Entity(
    model = 'plane',
    color = color.magenta,
    z = -.1,
    y = -3,
    origin = (0, .5),
    scale = (50, 1, 10),
    collider = 'box',
    )

app.run()                       # opens a window and starts the game.
