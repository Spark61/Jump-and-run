# Dateiname: main.py
# Version: 1.0
# Bearbeiter: Jan Fischer
# Datum: 05.09.2022

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
