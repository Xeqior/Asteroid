import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameLoop()

def gameLoop():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()



if __name__ == "__main__":
    main()
    