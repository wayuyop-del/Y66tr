import pygame
import random

class Monster:

    def __init__(self,x,y,type):

        self.rect = pygame.Rect(x,y,32,32)

        self.type = type

        if type=="zombie":
            self.speed = 1
            self.damage = 10

        elif type=="ghost":
            self.speed = 1
            self.damage = 999

        elif type=="spider":
            self.speed = 3
            self.damage = 15

    def update(self,player):

        if self.rect.x < player.rect.x:
            self.rect.x += self.speed

        if self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        if self.rect.y < player.rect.y:
            self.rect.y += self.speed

        if self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def draw(self,screen):

        if self.type=="zombie":
            color=(0,150,0)

        elif self.type=="ghost":
            color=(200,200,255)

        else:
            color=(200,0,0)

        pygame.draw.rect(screen,color,self.rect)
