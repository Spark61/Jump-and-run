# Dateiname: main.py
# Version: 1.0
# Bearbeiter: Jan Fischer
# Datum: 05.09.2022

import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Jump and Run")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    pygame.display.update()
    clock.tick(60)

pygame.quit()