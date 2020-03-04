from classes import *
import sys
from random import randint


pygame.init()

size = width,heigh = 400,400
screen = pygame.display.set_mode(size)
background_image = pygame.image.load(r"img/background.png")
bouncer = Bouncer()

ball = Ball()
clock = pygame.time.Clock()

bricks = []
for i in range(16):
    bricks.append(Brick(i*25,0, 1))
for i in range(0, 400, 22):
    bricks.append(Brick(i, 25, 0))
for i in range(0, 400, 22):
    bricks.append(Brick(i, 50, 3))
    
    
def Draw():
    screen.blit(background_image, [0,0])
    screen.blit(bouncer.bouncer, bouncer.rect)
    screen.blit(ball.ball, ball.rect)
    for i in range(len(bricks)):
        if bricks[i].verifica:
            pygame.draw.rect(screen, bricks[i].collor, bricks[i].brick)

lose = False

breaked = 0

while not lose:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_RIGHT]:
        bouncer.moveRight(width)
        
    elif pressed_keys[pygame.K_LEFT]:
        bouncer.moveLeft(width)
        
    #collisions
    if pygame.Rect.colliderect(ball.rect, bouncer.rect):
        ball.speed_y  = -1
        
    for i in range(len(bricks)):
        if pygame.Rect.colliderect(bricks[i].brick, ball.rect):
            if bricks[i].verifica:
                ball.rect.top += 2
                ball.speed_y = ball.speed_y * -1
            
                bricks[i].verifica = False
                breaked += 1
                
    if ball.rect.bottom == 400:
        lose = True
           
    ball.move()
    
    win = False
    if breaked >= 16:
        win = True
        ball.speed_x = 0
        ball.speed_y = 0
    if win:
        background_image = pygame.image.load(r"img/background_win.png")
        
    
    
    clock.tick(150)
    Draw()
    pygame.display.update()