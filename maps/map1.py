# -------------------------------------------------------------------------------
# Name:        map1.py
# Author:      Nico Hennig
# Created:     05.09.2022
# Copyright:   (c) Fischer, Gürschke, Hennig  2022
# -------------------------------------------------------------------------------
import os

import pygame

from enemy import Enemy
from mouse import Mouse
from platform import Platform


class Map1:
    def __init__(self):

        self.tiles = {}

        dir_path = "img/tiles/"

        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)) and path.endswith(".png"):
                self.tiles[path.replace(".png", "")] = pygame.transform.scale(pygame.image.load(dir_path + "/" + path),
                                                                              (32, 32))

        self.goal_pos_x = 100000

        self.cam_pos_x = 0
        self.positions = [(1, 28, 400, 1), (50, 26, 50, 3), (70, 18, 17, 3), (99, 25, 20, 4), (96, 14, 12, 5),
                          (118, 10, 7, 19), (123, 18, 88, 11), (283, 18, 88, 11), (258, 21, 30, 7)]

        self.platform_group = pygame.sprite.Group()

        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(Enemy(350, 425))

        for position in self.positions:
            x, y, width, height = position
            self.platform_group.add(Platform(x, y, width, height))

        self.mouse = Mouse(6350, 423)
        self.mouse_group = pygame.sprite.GroupSingle()
        self.mouse_group.add(self.mouse)

    def is_in_goal(self, player) -> bool:
        return player.rect.colliderect(self.mouse.rect)

    def update(self, screen, player_pos_x):
        self.cam_pos_x += 1

        self.enemy_group.update(player_pos_x)
        self.platform_group.update(screen, player_pos_x)
        self.platform_group.draw(screen)
        self.enemy_group.draw(screen)

        water = self.tiles["waterTop"]
        water_width = water.get_width()
        water_height = screen.get_height() - water.get_height()

        for i in range(player_pos_x + screen.get_width() // water_width + 1):
            screen.blit(water, (i * water_width - player_pos_x, water_height))
