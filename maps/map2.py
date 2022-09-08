# -------------------------------------------------------------------------------
# Name:        map2.py
# Created:     05.09.2022
# Copyright:   (c) Fischer, Gürschke, Hennig  2022
# -------------------------------------------------------------------------------
import os

import pygame

from enemy import Enemy
from mouse import Mouse
from platform import Platform


class Map2:
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
        self.positions = [(1, 28, 120, 2), (44, 22, 26, 6), (130, 26, 14, 2),
                          (150, 20, 15, 4), (180, 28, 40, 2), (200, 26, 30, 2), (202, 24, 38, 2), (204, 22, 20, 2),
                          (260, 28, 20, 2)]  ##Map2

        self.platform_group = pygame.sprite.Group()

        for position in self.positions:
            x, y, width, height = position
            self.platform_group.add(Platform(x, y, width, height))

        self.mouse = Mouse(4400, 423)
        self.mouse_group = pygame.sprite.GroupSingle()
        self.mouse_group.add(self.mouse)

        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(Enemy(350, 425))

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
