# -------------------------------------------------------------------------------
# Name:        enemy.py
# Author:      Jan Fischer
# Created:     07.09.2022
# Copyright:   Fischer, Gürschke, Hennig 2022
# -------------------------------------------------------------------------------

import os

import pygame
from pygame import sprite


def is_right(x, width):
    return x == width - 1


def is_left(x):
    return x == 0


def is_up(y):
    return y == 0


def is_down(y, height):
    return y == height - 1


def is_left_up(x, y):
    return is_left(x) and is_up(y)


def is_right_up(x, y, width):
    return is_right(x, width) and is_up(y)


def is_left_down(x, y, height):
    return is_left(x) and is_down(y, height)


def is_right_down(x, y, width, height):
    return is_right(x, width) and is_down(y, height)


def load_titles(dir_path):
    tiles = {}

    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)) and path.endswith(".png"):
            tiles[path.replace(".png", "")] = pygame.transform.scale(
                pygame.image.load(dir_path + "/" + path).convert_alpha(),
                (16, 16))

    return tiles


def is_small_island(height):
    return height == 1


class Platform(sprite.Sprite):
    def __init__(self, start_x, start_y, width, height):
        sprite.Sprite.__init__(self)

        self.tiles = load_titles("img/tiles/")

        if is_small_island(height):
            self.image = self.tiles["floatingLeft"]
        else:
            self.image = self.tiles["wallTopLeft"]

        self.texture_width = self.image.get_width()
        self.texture_height = self.image.get_height()

        self.full_width = self.texture_width * width
        self.full_height = self.texture_height * height

        self.start_x = start_x * self.texture_width
        self.start_y = start_y * self.texture_height

        self.blocks = []

        # rect
        self.rect = None
        self.rect_up = None
        self.rect_up_upper = None
        self.rect_down = None
        self.rect_left = None
        self.rect_right = None

        self.update_rects(0)  # werden in dieser Methode, auf die tatsächlichen Werte gesetzt

        self.rect.x = self.start_x
        self.rect.y = self.start_y

        if is_small_island(height):
            for x in range(width):
                if is_left(x):
                    tile = "floatingLeft"

                elif is_right(x, width):
                    tile = "floatingRight"

                else:
                    tile = "floatingMiddle"

                self.blocks.append([
                    self.start_x + self.texture_width * x,
                    self.start_y,
                    self.tiles[tile]
                ])
        else:
            for x in range(width):
                for y in range(height):
                    if is_left_up(x, y):
                        tile = "wallTopLeft"

                    elif is_right_up(x, y, width):
                        tile = "wallTopRight"

                    elif is_left_down(x, y, height):
                        tile = "bottomCornerLeft"

                    elif is_left(x):
                        tile = "wallLeft"

                    elif is_right_down(x, y, width, height):
                        tile = "bottomCornerRight"

                    elif is_right(x, width):
                        tile = "wallRight"

                    elif is_down(y, height):
                        tile = "bottomMiddle"

                    elif is_up(y):
                        tile = "wallTopMiddle"

                    else:
                        tile = "wallMiddle"

                    self.blocks.append([
                        self.start_x + self.texture_width * x,
                        self.start_y + self.texture_height * y,
                        self.tiles[tile]
                    ])

    def update_rects(self, cam_pos_x):
        self.rect = pygame.Rect(self.start_x - cam_pos_x, self.start_y, self.full_width, self.full_height)
        self.rect2 = pygame.Rect(self.start_x - cam_pos_x, self.start_y, self.full_width, self.full_height - 6)

        self.rect_up = pygame.Rect(self.start_x - cam_pos_x, self.start_y + 1, self.full_width, 1)
        self.rect_up_upper = pygame.Rect(self.start_x - cam_pos_x, self.start_y, self.full_width, 10)
        self.rect_down = pygame.Rect(self.start_x - cam_pos_x, self.start_y + self.full_height - 1, self.full_width, 1)
        self.rect_left = pygame.Rect(self.start_x - 1 - cam_pos_x, self.start_y + 5, 2, self.full_height - 10)
        self.rect_right = pygame.Rect(self.start_x + self.full_width - 1 - cam_pos_x, self.start_y + 5, 1,
                                      self.full_height - 10)

    def draw_blocks(self, screen, cam_pos_x):
        for block in self.blocks:
            x, y, texture = block
            screen.blit(texture, (x - cam_pos_x, y))

    def update(self, screen, cam_pos_x):
        self.update_rects(cam_pos_x)
        self.draw_blocks(screen, cam_pos_x)
