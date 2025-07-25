# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))



    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()



        # limit framerate to 60 FPS
        dt = clock.tick(60.0) / 1000


if __name__ == "__main__":
    main()