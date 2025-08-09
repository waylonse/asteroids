from circleshape import CircleShape
from constants import *
import pygame
from main import updatable, drawable, shots
from shot import Shot


class Player(CircleShape):


    def __init__(self, x, y, radius, updatable_group, drawable_group, shots_group):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.updatable_group = updatable_group
        self.drawable_group = drawable_group
        self.shots_group = shots_group
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # Wrap around screen edges
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
    
    def update(self, dt):
        self.shoot_timer += dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        if self.shoot_timer < 0.3:
            return
        else:
            self.shoot_timer = 0
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot_position = self.position + forward * self.radius
            shot_velocity = forward * PLAYER_SHOOT_SPEED
            shot = Shot(shot_position.x, shot_position.y, SHOT_RADIUS)
            shot.velocity = shot_velocity
            self.updatable_group.add(shot)
            self.drawable_group.add(shot)
            self.shots_group.add(shot)