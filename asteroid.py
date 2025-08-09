from circleshape import *
from constants import *
import pygame
import random


class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self):
        """Split the asteroid into two smaller ones."""
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius / 2
            angle = random.uniform(0, 360)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1
            asteroid2.velocity = velocity2
            return [asteroid1, asteroid2]
        return []
