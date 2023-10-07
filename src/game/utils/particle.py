import pygame

class RainbowParticles:

    def __init__(self):
        self.particles = []
        self.size = 4
        self.scroll_speed = 4
        self.x = 90

    def draw(self, screen, catY):
        self.generate_particles(catY)
        self.delete_particles()
        for particle in self.particles:
            particle[0].x -= self.scroll_speed
            pygame.draw.rect(screen, particle[1], particle[0])

    def generate_particles(self, catY):
        colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
        init_offset = 6
        for color in colors: 
            self.add_particles(init_offset + self.size, pygame.Color(color), catY)
            init_offset +=  self.size

    def add_particles(self, offset, color, catY):
        pos_y = catY + offset
        particle_rect = pygame.Rect(self.x - self.size // 2, pos_y - self.size // 2, self.size, self.size)
        self.particles.append((particle_rect, color))

    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[0].x > 0]
