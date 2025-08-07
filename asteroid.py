import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, color=(255,255,255), center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_x = self.position.x
        old_y = self.position.y
        self.kill()
        if old_radius <=ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(old_x, old_y, new_radius)
            asteroid1.velocity *= 1.2
            asteroid1.velocity = self.velocity.rotate(random.uniform(20, 50))
            asteroid2 = Asteroid(old_x, old_y, new_radius)
            asteroid2.velocity *= 1.2
            asteroid2.velocity = self.velocity.rotate(-random.uniform(-20, -50))
            return asteroid1, asteroid2
