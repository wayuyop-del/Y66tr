import pygame

class Boss:

    def __init__(self,x,y):

        self.rect = pygame.Rect(x,y,80,80)

        self.hp = 500

        self.speed = 2

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

        pygame.draw.rect(screen,(255,0,200),self.rect)
