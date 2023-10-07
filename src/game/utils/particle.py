import pygame

class RainbowParticles:

    def __init__(self):
        self.particles = []
        self.size = 4
        self.x = 90

    def draw(self, screen, catY):
        self.generate_particles(catY)
        self.delete_particles()
        for particle in self.particles:
            particle[0].x -= 4
            pygame.draw.rect(screen, particle[1], particle[0])

    def generate_particles(self, catY):
        self.add_particles(6, pygame.Color('Red'), catY)
        self.add_particles(10, pygame.Color('Orange'), catY)
        self.add_particles(14, pygame.Color('Yellow'), catY)
        self.add_particles(18, pygame.Color('Green'), catY)
        self.add_particles(22, pygame.Color('Blue'), catY)
        self.add_particles(26, pygame.Color('Purple'), catY)

    def add_particles(self, offset, color, catY):
        pos_y = catY + offset
        particle_rect = pygame.Rect(self.x - self.size // 2, pos_y - self.size // 2, self.size, self.size)
        self.particles.append((particle_rect, color))

    def delete_particles(self):
        self.particles = [particle for particle in self.particles if particle[0].x > 0]
