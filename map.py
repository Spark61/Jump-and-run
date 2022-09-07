# -------------------------------------------------------------------------------
# Name:        map.py
# Created:     05.09.2022
# Copyright:   (c) Fischer, Gürschke, Hennig  2022
# -------------------------------------------------------------------------------
import os

import pygame

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

        print(self.tiles)

        self.cam_pos_x = 0
        self.positions = [(1, 1, 30, 1), (100, 1, 30, 2)]
        self.platform_group = pygame.sprite.Group()

        for position in self.positions:
            x, y, width, height = position
            self.platform_group.add(Platform(x, y, width, height))

    def update(self, screen, player_pos_x):

        self.cam_pos_x += 1

        self.platform_group.update(screen, player_pos_x)
        self.platform_group.draw(screen)
