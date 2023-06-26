from pygame import *

window = display.set_mode((700, 500))
window.fill((0, 179, 255))

clock = time.Clock()
FPS = 120

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
