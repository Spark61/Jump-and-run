import os

import pygame
from pygame import sprite


class Platform(sprite.Sprite):
    def __init__(self, start_x, start_y, width, height):
        sprite.Sprite.__init__(self)

        self.tiles = {}

        dir_path = "img/tiles/"

        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)) and path.endswith(".png"):
                self.tiles[path.replace(".png", "")] = pygame.transform.scale(pygame.image.load(dir_path + "/" + path),
                                                                              (32, 32))
        if height == 1:
            self.image = self.tiles["floatingLeft"]
        else:
            self.image = self.tiles["wallTopLeft"]

        texture_width = self.image.get_width()
        texture_height = self.image.get_height()

        self.blocks = []
        self.rect = pygame.Rect(start_x, start_y, texture_width * width, texture_height * height)

        self.rect.x = start_x
        self.rect.y = start_y

        if height == 1:
            for x in range(width):
                print(x)
                if x == 0:
                    self.blocks.append([
                        start_x + texture_width * x,
                        start_y,
                        self.tiles["floatingLeft"]
                    ])
                elif x == width - 1:
                    self.blocks.append([
                        start_x + texture_width * x,
                        start_y,
                        self.tiles["floatingRight"]
                    ])
                else:
                    self.blocks.append([
                        start_x + texture_width * x,
                        start_y,
                        self.tiles["floatingMiddle"]
                    ])

        else:
            for x in range(width):
                for y in range(height):
                    if x == 0 and y == 0:
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["wallTopLeft"]
                        ])
                    elif x == width - 1 and y == 0:
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["wallTopRight"]
                        ])
                    elif x == 0 and y == height - 1:
                        print(x, y)
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["bottomCornerLeft"]
                        ])
                    elif x == 0:
                        print(x, y)
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["wallLeft"]
                        ])
                    elif x == width - 1 and y == height - 1:
                        print(x, y)
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["bottomCornerRight"]
                        ])
                    elif x == width - 1:
                        print(x, y)
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["wallRight"]
                        ])
                    elif y == height - 1:
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["bottomMiddle"]
                        ])
                    elif y != 0:
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["wallMiddle"]
                        ])
                    else:
                        self.blocks.append([
                            start_x + texture_width * x,
                            start_y + texture_height * y,
                            self.tiles["wallTopMiddle"]
                        ])

    def update(self, screen):
        for block in self.blocks:
            x, y, texture = block
            screen.blit(texture, (x, y))
