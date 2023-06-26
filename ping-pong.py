from pygame import *

window = display.set_mode((700, 500))
window.fill((0, 179, 255))

clock = time.Clock()
FPS = 120

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x=65, size_y=65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y < 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.x > 420:
            self.rect.y += self.speed

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
