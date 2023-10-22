import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y, position, y_speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.x = x
        self.y = y
        self.position = position
        self.scroll_speed = 4
        self.pipe_gap = 150
        self.rect = self.image.get_rect()
        self.direction = direction
        self.y_speed = y_speed

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
        
    def change_direction(self):
        self.direction *= -1

    def stop_moving(self):
        self.y_speed = 0

    def move(self):
        self.rect.y += (self.direction * self.y_speed)

        if self.position == 1:
            if self.rect.bottomleft[1] <= 0:
                self.change_direction()
            if self.rect.bottomleft[1] + self.pipe_gap >= 700:
                self.change_direction()
        else:
            if self.rect.topleft[1] - self.pipe_gap <= 0:
                self.change_direction()
            if self.rect.topleft[1] >= 700:
                self.change_direction()