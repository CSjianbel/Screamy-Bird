import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, sprite, x, y, position, bird):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.bird = bird
        self.x = x
        self.y = y
        self.position = position
        self.scroll_speed = 4
        self.bird_dashed = False
        self.last_dashed = pygame.time.get_ticks() - 1000
        self.pipe_gap = 200
        self.velocity = 0
        self.midpoint = 350
        self.can_close = True
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

        if self.bird_dashed:
            time_now = pygame.time.get_ticks()
            if time_now - self.last_dashed > 200:
                self.bird.velocity = 0
                self.bird_dashed = False
                self.scroll_speed = 4

        if self.position == 1:
            if self.rect.bottom != self.midpoint:
                self.rect.y += self.velocity
                if self.rect.bottom == (self.y - int(self.pipe_gap / 2)):
                    self.velocity = 0
                    self.can_close = True

            if self.rect.bottom == self.midpoint:
                self.rect.y -= self.velocity
                self.velocity = -5
        else:
            if self.rect.top != self.midpoint:
                self.rect.y -= self.velocity
                if self.rect.top == (self.y + int(self.pipe_gap / 2)):
                    self.velocity = 0
                    self.can_close = True

            if self.rect.top == self.midpoint:
                self.rect.y += self.velocity
                self.velocity = -5

        if self.rect.right < 0:
            self.kill()

    def closePipe(self):
        self.can_close = False
        self.velocity = 5
    
    def fasterPipes(self):
        self.bird_dashed = True
        self.scroll_speed = 12
        self.last_dashed = pygame.time.get_ticks()