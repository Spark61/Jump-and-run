import pygame
from pygame import sprite


class Mouse(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.idle_textures = []
        self.idle_texture_width = 16
        self.texture_height = 16

        idle_full_image = pygame.image.load("img/player/mouse/mouse_0_walk.png").convert_alpha()

        for i in range(idle_full_image.get_width() // self.idle_texture_width):
            self.idle_textures.append(pygame.transform.flip(pygame.transform.scale(
                idle_full_image.subsurface(i * self.idle_texture_width, 0, self.idle_texture_width,
                                           self.texture_height),
                (self.idle_texture_width * 3, self.texture_height * 3)), True, False))

        self.image = self.idle_textures[0]
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.rect.center = (x, y)

        self.idle_animation_index = 1

    def update_image(self):
        self.idle_animation_index += 1

        if self.idle_animation_index >= 20:
            self.idle_animation_index = 0

        self.image = self.idle_textures[(self.idle_animation_index // 10)]

    def update_position(self, player_pos_x):
        self.rect.x = self.pos_x - player_pos_x

    def update(self, player_pos_x):
        self.update_position(player_pos_x)
        self.update_image()
