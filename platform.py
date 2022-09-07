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
                self.tiles[path.replace(".png", "")] = pygame.transform.scale(
                    pygame.image.load(dir_path + "/" + path).convert_alpha(),
                    (16, 16))
        if height == 1:
            self.image = self.tiles["floatingLeft"]
        else:
            self.image = self.tiles["wallTopLeft"]

        self.texture_width = self.image.get_width()
        self.texture_height = self.image.get_height()

        start_x = start_x * self.texture_width
        start_y = start_y * self.texture_height

        self.start_x = start_x
        self.start_y = start_y
        self.width = self.texture_width * width
        self.height = self.texture_height * height

        self.blocks = []
        self.rect = pygame.Rect(start_x, start_y, self.width, self.height)

        self.rect.x = start_x
        self.rect.y = start_y

        if height == 1:
            for x in range(width):
                if x == 0:  # links
                    self.blocks.append([
                        self.start_x + self.texture_width * x,
                        self.start_y,
                        self.tiles["floatingLeft"]
                    ])
                elif x == width - 1:  # rechts
                    self.blocks.append([
                        self.start_x + self.texture_width * x,
                        self.start_y,
                        self.tiles["floatingRight"]
                    ])
                else:  # mitte
                    self.blocks.append([
                        self.start_x + self.texture_width * x,
                        self.start_y,
                        self.tiles["floatingMiddle"]
                    ])

        else:
            for x in range(width):
                for y in range(height):
                    if x == 0 and y == 0:  # links oben
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["wallTopLeft"]
                        ])
                    elif x == width - 1 and y == 0:  # rechts oben
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["wallTopRight"]
                        ])
                    elif x == 0 and y == height - 1:  # links unten
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["bottomCornerLeft"]
                        ])
                    elif x == 0:  # linke Seite
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["wallLeft"]
                        ])
                    elif x == width - 1 and y == height - 1:  # rechts unten
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["bottomCornerRight"]
                        ])
                    elif x == width - 1:  # rechte Seite
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["wallRight"]
                        ])
                    elif y == height - 1:  # untere Seite
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["bottomMiddle"]
                        ])
                    elif y == 0:  # obere Seite
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["wallTopMiddle"]
                        ])
                    else:  # mitte
                        self.blocks.append([
                            self.start_x + self.texture_width * x,
                            self.start_y + self.texture_height * y,
                            self.tiles["wallMiddle"]
                        ])

    def update(self, screen, cam_pos_x):
        self.rect = pygame.Rect(self.start_x - cam_pos_x, self.start_y, self.width, self.height)

        for block in self.blocks:
            x, y, texture = block
            screen.blit(texture, (x - cam_pos_x, y))
