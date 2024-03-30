from pygame import *
win_hieght = 600
win_wieght = 500
window = display.set_mode((win_wieght, win_hieght))
back =(200, 200, 255)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size_x, player_size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size_x, player_size_y))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <440:
            self.rect.y += self.speed  
class Player2(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <440:
            self.rect.y += self.speed 



levish = Player('palka.png', 5, 200, 3, 20, 160)
pravish = Player2('palka.png', 475, 200, 3, 20, 160) 
clock = time.Clock()
game = True
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    levish.update_l()
    pravish.update_r()

    levish.reset()

    pravish.reset()
    display.update()
    clock.tick(180)
