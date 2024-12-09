import pygame
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import *
from player import Player

def main():
    pygame.init()

    # define groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                return
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides(bullet):
                    asteroid.split()
                    bullet.kill()
                    print("collision")

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
