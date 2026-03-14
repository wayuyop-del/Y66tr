import pygame
from settings import *

class Player:

    def __init__(self,x,y):

        self.rect = pygame.Rect(x,y,32,32)

        self.hp = PLAYER_HP

        self.speed = PLAYER_SPEED

        self.coke = 4
        self.shield = 4
        self.revive = 4
        self.time_stop = 3

        self.speed_timer = 0
        self.shield_timer = 0

    def move(self,keys):

        move = self.speed

        if self.speed_timer>0:
            move = 9
            self.speed_timer -=1

        if keys[pygame.K_w]:
            self.rect.y -= move

        if keys[pygame.K_s]:
            self.rect.y += move

        if keys[pygame.K_a]:
            self.rect.x -= move

        if keys[pygame.K_d]:
            self.rect.x += move

    def draw(self,screen):

        pygame.draw.rect(screen,(0,255,0),self.rect)
