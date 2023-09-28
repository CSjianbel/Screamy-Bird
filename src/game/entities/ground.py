import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y, game_status):
        pygame.sprite.Sprite.__init__(self)
        self.game_status = game_status
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.ground_scroll = 0
        self.ground_scroll_speed = 4

    def update(self):
        if self.game_status.is_game_started or self.game_status.is_game_idle:
            self.rect.x -= self.ground_scroll_speed
            if (abs(self.rect.x) > 35):
                self.rect.x = 0