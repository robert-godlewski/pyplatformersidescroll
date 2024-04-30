import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, color, width: int, height: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        # Need to flush this out
