import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, sprite, init_x, init_y, game_status, game_manager):
        pygame.sprite.Sprite.__init__(self)
        self.game_status = game_status
        self.game_manager = game_manager
        self.images = sprite
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = [init_x, init_y]
        self.index = 0
        self.init_x = init_x
        self.init_y = init_y
        self.counter = 0
        self.velocity = 0

    def update(self):
        if not self.game_status.is_game_over:
            self.animate_bird()

        if (self.game_manager.game_mode == "voice" or self.game_manager.game_mode == "tap"):
            if self.game_status.is_game_started or self.game_status.is_game_over:
                self.apply_gravity()
        
        if (self.game_manager.game_mode == "cam"):
            #bird_pos = self.game_manager.nose_detection.get_nose_pos()
            #self.rect.x = bird_pos[0]
            #self.rect.y = bird_pos[1]
            pass

        self.rotate()
        self.check_bounds()

    # make the bird jump
    def jump(self):
        self.game_status.set_game_started()
        self.velocity = -9

    # apply gravity to the bird
    def apply_gravity(self):
        self.velocity += 0.5
        self.rect.y += self.velocity

    # animate the bird
    def animate_bird(self):
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

    # avoid bird to go beyond the screen
    def check_bounds(self):
        if self.rect.bottom >= 685:
            self.rect.bottom = 685
        if self.rect.top <= 0:
            self.rect.top = 0

    def rotate(self):
        if self.game_status.is_game_started:
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)
        if self.game_status.is_game_over:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

    # reset bird's position
    def reset(self):
        self.rect.y = 450
        self.rect.center = [self.init_x, self.init_y]
        self.velocity = 0
        self.game_status.set_game_idle()

    def getPosY(self):
        return self.rect.y
    
    # cinacall ito sa nose_detection.py
    def setPos(self, pos):
        if pos != None:
            self.rect.x = pos[0]
            self.rect.y = pos[1]
        print(self.rect)
