import pygame
import random

from settings import *
from player import Player
from monster import Monster
from boss import Boss
from maze import generate_maze
from ui import draw_ui

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

player = Player(400,300)

monsters = []

for i in range(10):

    t = random.choice(["zombie","ghost","spider"])

    monsters.append(
        Monster(random.randint(0,900),random.randint(0,600),t)
    )

boss = Boss(800,500)

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False

    keys = pygame.key.get_pressed()

    player.move(keys)

    screen.fill((0,0,0))

    player.draw(screen)

    for m in monsters:

        m.update(player)
        m.draw(screen)

        if player.rect.colliderect(m.rect):

            player.hp -= m.damage

    boss.update(player)
    boss.draw(screen)

    draw_ui(screen,player)

    pygame.display.update()

pygame.quit()
