import pygame
from utils import Direction

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = Direction.RIGHT

    def change_direction(self, key):
        if key == pygame.K_UP and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif key == pygame.K_DOWN and self.direction != Direction.UP:
            self.direction = Direction.DOWN
        elif key == pygame.K_LEFT and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif key == pygame.K_RIGHT and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == Direction.UP:
            head_y -= 10
        elif self.direction == Direction.DOWN:
            head_y += 10
        elif self.direction == Direction.LEFT:
            head_x -= 10
        elif self.direction == Direction.RIGHT:
            head_x += 10
        self.body = [(head_x, head_y)] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self, position):
        return self.body[0] == position

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))
