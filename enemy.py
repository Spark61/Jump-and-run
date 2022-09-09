# -------------------------------------------------------------------------------
# Name:        enemy.py
# Author:      David Gürschke
# Created:     07.09.2022
# Copyright:   Fischer, Gürschke, Hennig 2022
# -------------------------------------------------------------------------------
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.full_image = pygame.image.load("img/player/cat_skele/cat_skele_walk.png").convert_alpha()

        self.direction = -1
        self.current_step = 0
        self.max_step = 50
        self.animation_index = 0

        self.posX = x

        self.texture_width = 17
        self.texture_height = 16

        self.animation = []

        for i in range(self.full_image.get_width() // self.texture_width):
            self.animation.append(pygame.transform.scale(
                self.full_image.subsurface(i * self.texture_width, 0, self.texture_width, self.texture_height),
                (self.texture_width * 3, self.texture_height * 3)))

        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.rect_front = pygame.Rect(self.rect.x, self.rect.y + 10, self.rect.width, self.rect.height)
        self.rect_top = pygame.Rect(self.rect.x + 5, self.rect.y, self.rect.width - 10, self.rect.height)

        self.rect.center = (x, y)

    def calc_shift(self, cameraPos):
        self.diff_x = cameraPos

    def update(self, player_pos_x):
        if self.current_step <= 0:
            self.direction *= -1
            self.current_step = 0
        if self.current_step > self.max_step:
            self.direction *= -1
            self.current_step = self.max_step
        self.animation_index += 0.1

        self.current_step += self.direction * 0.4

        if self.animation_index >= 35:
            self.animation_index = 0

        if self.direction > 0:
            self.image = self.animation[int(self.animation_index) // 5]
        else:
            self.image = pygame.transform.flip(self.animation[int(self.animation_index) // 5], True, False)

        self.rect.x = self.posX - player_pos_x + self.current_step
        self.rect_front = pygame.Rect(self.rect.x, self.rect.y + 10, self.rect.width, self.rect.height)
        self.rect_top = pygame.Rect(self.rect.x + 5, self.rect.y, self.rect.width - 10, self.rect.height)

    def get_hitbox(self):
        return (self.rect_front, self.rect_top)
