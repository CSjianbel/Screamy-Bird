# Import libraries
import os
import random

import pygame

import base
import pipe
import bird


# pygame setup
pygame.init()
HEIGHT, WIDTH = 800, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Screamy Bird!")

BG_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "bg.png")).convert_alpha(), (WIDTH, HEIGHT))
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join(
    "assets", f"bird{i}.png")).convert_alpha()) for i in range(1, 4)]
BASE_IMG = pygame.transform.scale2x(pygame.image.load(
    os.path.join("assets", "base.png")).convert_alpha())
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(
    os.path.join("assets", "pipe.png")).convert_alpha())

# The main function of the program


def main():
    CLOCK = pygame.time.Clock

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.blit(BG_IMG, (0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
