import pygame


class Character(pygame.sprite.Sprite):
    def __init__(self, color: tuple, width: int, height: int, position_x: int, position_y: int):
        super().__init__()
        # For now just use a rectangle
        self.color = color
        self.rect = pygame.Rect(position_x,position_y,width,height)
        self.x_velocity = 0
        self.y_velocity = 0
        self.gravity = -9.8
        self.fall_count = 0

    def draw(self, surface) -> pygame.Rect:
        pygame.draw.rect(surface, color=self.color, rect=self.rect)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, dt):
        self.rect.x -= 300 * dt

    def move_right(self, dt):
        self.rect.x += 300 * dt

    def gravity_affect(self, fps):
        self.y_velocity += (self.fall_count/fps)*self.gravity
        self.move(self.x_velocity, -self.y_velocity)
        self.fall_count += 1
