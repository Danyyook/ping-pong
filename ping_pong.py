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
speed_x = 3
speed_y = 3



levish = Player('palka.png', 5, 200, 3, 20, 160)
pravish = Player2('palka.png', 475, 200, 3, 20, 160) 
ball = GameSprite('kake.png', 120,120,3,50,50)
clock = time.Clock()
font.init()
font1 = font.Font(None, 50)
lose1 = font1.render('PLayer 1 lose', True, (0,0,0))
font2 = font.Font(None, 50)
lose2 = font2.render('PLayer 2 lose', True, (0,0,0))
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(levish, ball) or sprite.collide_rect(pravish, ball):
            speed_x *= -1
            speed_y*= 1
        if ball.rect.y > win_hieght - 50 or ball.rect.y < 0:
            speed_y *= -1
            speed_x *= 1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > win_hieght-50:
            finish = True
            window.blit(lose2, (200,200))
        levish.update_l()
        pravish.update_r()
        levish.reset()
        pravish.reset()
        ball.reset()
    display.update()
    clock.tick(60)
