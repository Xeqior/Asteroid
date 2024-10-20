import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
import sys


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameLoop()

def gameLoop():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    delta = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 
    Asteroid.containers = (updatable, drawable,asteroids)
    Shot.containers = (updatable,drawable,shots)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH /2,SCREEN_HEIGHT /2)
    asteroidfield = AsteroidField()
    #updatable.add(player)
    #drawable.add(player)

    dt = 0

    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        dt = delta.tick(60) / 1000
        updateGroups(updatable,dt)
        drawGroups(drawable,screen)
        collided(asteroids, player)
        bulletCollision(asteroids,shots)
        pygame.display.flip()

def updateGroups(updatable,dt):
    for object in updatable:
        object.update(dt)

def drawGroups(drawable,screen):
    for object in drawable:
        object.draw(screen)
def collided(asteroids, player):
    for obj in asteroids:
        if(obj.collision(player)):
            print("Game over!")
            sys.exit()

def bulletCollision(asteroids,bullets):
    for obj in asteroids:
        for bullet in bullets:
            if(obj.collision(bullet)):
                obj.split()
                bullet.kill()
    

if __name__ == "__main__":
    main()

    