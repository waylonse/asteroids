import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

# Important Constants
clock = pygame.time.Clock()
dt = 0

# Make groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)
    updatable.add(player)
    drawable.add(player)
    asteroidfield = AsteroidField(updatable, drawable)
    updatable.add(asteroidfield)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)  # Call the custom draw method
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        updatable.update(dt)
        pygame.display.set_caption(f"Asteroids - FPS: {clock.get_fps():.2f}")


if __name__ == "__main__":
    main()
