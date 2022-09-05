# Dateiname: main.py
# Version: 1.0
# Bearbeiter: Jan Fischer
# Datum: 05.09.2022

import pygame

from player import Player

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump and Run")

running = True
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.walk_x(-1)
            elif event.key == pygame.K_d:
                player.walk_x(1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.walk_x(0)

    screen.fill((255, 255, 255))

    player_group.update()
    player_group.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
