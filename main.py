# Dateiname: main.py
# Version: 1.0
# Bearbeiter: Jan Fischer
# Datum: 05.09.2022

import pygame

from platform import Platform
from player import Player

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump and Run")

running = True
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

platform = Platform(100, 100, 4, 4)
platform_group = pygame.sprite.Group()
platform_group.add(platform)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.walk_x(-1)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.walk_x(1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.walk_x(0)

    screen.fill((255, 255, 255))

    player_group.update()
    player_group.draw(screen)

    platform_group.update(screen)
    platform_group.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
