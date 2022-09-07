import pygame
from pygame import sprite


class Player(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.walk_textures = []
        self.run_textures = []
        self.walk_texture_width = 17
        self.run_texture_width = 20
        self.texture_height = 16

        walk_full_image = pygame.image.load("img/player/cat_0/cat_0_walk.png").convert_alpha()
        run_full_image = pygame.image.load("img/player/cat_0/cat_0_run.png").convert_alpha()

        for i in range(walk_full_image.get_width() // self.walk_texture_width):
            self.walk_textures.append(pygame.transform.scale(
                walk_full_image.subsurface(i * self.walk_texture_width, 0, self.walk_texture_width,
                                           self.texture_height),
                (self.walk_texture_width * 3, self.texture_height * 3)))

        for i in range(walk_full_image.get_width() // self.run_texture_width):
            self.run_textures.append(pygame.transform.scale(
                run_full_image.subsurface(i * self.run_texture_width, 0, self.run_texture_width,
                                          self.texture_height), (self.run_texture_width * 3, self.texture_height * 3)))

        self.image = self.run_textures[0]
        self.rect = self.image.get_rect()

        self.speed = 10
        self.posX = 200
        self.posY = 400

        self.jumping = -1
        self.walk = 0
        self.left = True

        self.run_animation_index = 1

    def walk_x(self, x):
        self.walk = x

        if x != 0:
            self.left = x < 0

    def jump(self):
        if self.jumping != -1:
            return

        self.jumping = 10

    def update_image(self):
        if self.walk != 0:
            self.run_animation_index += 1

            if self.run_animation_index >= 30:
                self.run_animation_index = 0

            if self.jumping != -1:
                pass
            else:
                self.image = self.run_textures[self.run_animation_index // 5]

        else:
            self.image = self.walk_textures[0]

        if self.left:
            self.image = pygame.transform.flip(self.image, True, False)

    def update_position(self):
        self.posX += self.walk * self.speed

        self.rect.x = self.posX
        self.rect.y = self.posY

    def update(self):
        self.update_position()
        self.update_image()
