from circleshape import *
from constants import *
import pygame


class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
