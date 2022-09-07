import pygame
from pygame import sprite


def is_collide_down(rect, platform):
    return rect.colliderect(platform.rect_down)


def is_collide_top(rect, platform):
    return rect.colliderect(platform.rect_up)


def is_collide_right(rect, platform):
    return rect.colliderect(platform.rect_right)


def is_collide_left(rect, platform):
    return rect.colliderect(platform.rect_left)


def is_rect_stand_on_block(platform_group, under_player_rect):
    for platform in platform_group:
        if under_player_rect.colliderect(platform.rect_up_upper):
            return True

    return False


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
        self.posY = 300

        self.jumping = False
        self.falling = False
        self.jump_index = 0
        self.walk = 0
        self.left = True

        self.run_animation_index = 1

    def walk_x(self, x):
        self.walk = x

        if x != 0:
            self.left = x < 0

    def jump(self):
        if self.jumping:
            return

        self.jumping = True
        self.falling = False
        self.jump_index = 0

    def is_gravity_active(self, screen, platform, platform_group, new_pos_x):
        if self.jumping:  # wenn er Springt, dann wird durch den jump_index, die Schwerkraft geregelt
            return False

        if self.rect.y >= platform.rect_up.y:  # ist der block nicht unter dem Player
            return False

        under_player_rect = pygame.Rect(self.rect.x + new_pos_x - 1, self.rect.y + self.rect.height + 2,
                                        self.rect.width - 1, 1)

        if under_player_rect.colliderect(platform.rect_up):  # wenn er auf einen
            return False

        if not is_collide_top(pygame.Rect(self.rect.x + new_pos_x - 1, 0,
                                          self.rect.width - 1,
                                          screen.get_height()), platform):
            return False

        return not is_rect_stand_on_block(platform_group, under_player_rect)

    def update_image(self):
        if self.walk != 0:
            self.run_animation_index += 1

            if self.run_animation_index >= 30:
                self.run_animation_index = 0

            self.image = self.run_textures[self.run_animation_index // 5]

        else:
            self.image = self.walk_textures[0]

        if self.left:
            self.image = pygame.transform.flip(self.image, True, False)

    def update_position(self, screen, map):
        new_pos_x = self.walk * self.speed

        rect = pygame.Rect(self.rect.x + new_pos_x - 1, self.rect.y, self.rect.width - 1, self.rect.height)

        for platform in map.platform_group:

            if is_collide_top(rect, platform) and \
                    not is_collide_left(rect, platform) and \
                    not is_collide_right(rect, platform):  # block oben
                self.falling = False
                self.jumping = False
                self.posY = platform.rect_up.y - platform.rect_up.height - self.rect.height

            elif self.is_gravity_active(screen, platform, map.platform_group,
                                        new_pos_x):  # springt nicht, ist aber auch auf keinen block drauf
                pygame.draw.rect(screen, (0, 0, 0), platform.rect_up_upper)
                self.posY += 5

            if is_collide_down(rect, platform):  # unten block
                self.falling = True

            if is_collide_left(rect, platform) and not is_collide_down(rect, platform):  # links blockd
                new_pos_x = platform.rect_left.x - (self.rect.x + self.rect.width)

            if is_collide_right(rect, platform) and not is_collide_down(rect, platform):  # rechts block
                new_pos_x = platform.rect_right.x - self.rect.x

        self.posX += new_pos_x
        if self.posX <= 0:
            self.posX = 0

        self.rect.x = screen.get_width() / 2

        if self.jumping:
            if self.falling and self.jump_index <= 0:
                self.falling = False
                self.jumping = False
            elif self.falling:
                self.jump_index -= 1
            elif self.jump_index >= 20:
                self.falling = True
            else:
                self.jump_index += 1

            self.rect.y = self.posY + -self.jump_index * 10
        else:
            self.rect.y = self.posY

    def update(self, screen, map):
        self.update_position(screen, map)
        self.update_image()
