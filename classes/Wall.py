import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))