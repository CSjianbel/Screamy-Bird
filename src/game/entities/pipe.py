import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.x = x
        self.y = y
        self.position = position
        self.scroll_speed = 4
        self.pipe_gap = 150
        self.rect = self.image.get_rect()

        # pipe will be placed at the top
        if self.position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(self.pipe_gap / 2)]
        # pipe will be placed at the bottom
        else:
            self.rect.topleft = [x, y + int(self.pipe_gap / 2)]
        
    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()