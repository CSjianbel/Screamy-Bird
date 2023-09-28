class Background:
    def __init__(self, sprite):
        self.background_sprite = sprite
    
    def draw(self, screen):
        screen.blit(self.background_sprite, (0, 0))
