import pygame
from random import randint

class Bouncer:
    def __init__(self):
        # size 30x10
        self.bouncer = pygame.image.load(r"img/bouncer.png")
        self.rect = self.bouncer.get_rect()
        self.speed_x = 2
        self.rect.top = 370
        self.rect.left = 200
    def moveLeft(self, width):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed_x
        
    def moveRight(self, width):
        if self.rect.right >= width:
            self.rect.right = width
        else:    
            self.rect.left += self.speed_x
            
            
class Ball:
    
    def __init__(self):
        self.ball = pygame.image.load(r"img/ball.png")
        self.rect = self.ball.get_rect()
        self.speed_x = 1
        self.speed_y = 1
        self.rect.left = 205
        self.rect.top = 360
        
        
    def move(self):
        if self.rect.left == 0:
            self.speed_x = 1
        elif self.rect.right == 400:
            self.speed_x = -1
        elif self.rect.bottom == 400:
            self.speed_y = -1
        elif self.rect.top == 0:
            self.speed_y = 1
            
        self.rect.left += self.speed_x
        self.rect.top += self.speed_y
        
    
class Brick:
    
    def __init__(self, pos_x, pos_y, collor):
        self.colors = [[17,0,241],[0,241,8],[255,255,0],[255,136,0],[0,241,255]]
        self.brick = pygame.Rect(pos_x, pos_y, 20, 15)
        self.collor = self.colors[collor]
        self.verifica = True