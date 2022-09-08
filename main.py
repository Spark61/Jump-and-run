# Dateiname: main.py
# Version: 1.0
# Bearbeiter: Jan Fischer
# Datum: 05.09.2022

import pygame

from maps.map1 import Map1
from maps.map2 import Map2
from maps.map3 import Map3
from player import Player

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump and Run")

running = True
clock = pygame.time.Clock()

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

maps = [Map1(), Map2(), Map3()]
map_number = 1

won = False
font = pygame.font.SysFont('Comic Sans MS', 40)
won_text_surface = font.render('Du hast Gewonnen!', False, (0, 0, 0))
lose_text_surface = font.render('Du bist gestorben!', False, (0, 0, 0))


def has_next_map():
    return len(maps) > (map_number + 1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.walk_x(-1)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.walk_x(1)
            elif event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.walk_x(0)

    screen.fill((255, 255, 255))

    if won:
        screen.blit(won_text_surface, (82, 150))
    else:
        map = maps[map_number]
        player_group.update(screen, map)

        if map.is_in_goal(player):
            if has_next_map():
                map_number += 1
                player.reset()
            else:
                won = True

        map.update(screen, player.posX)

        player_group.draw(screen)

        map.mouse_group.update(player.posX)
        map.mouse_group.draw(screen)
        print(map.mouse.rect)

        if player.death:
            screen.blit(lose_text_surface, (82, 150))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
