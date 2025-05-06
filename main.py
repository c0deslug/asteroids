# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    AstroClock = pygame.time.Clock()
    dt = 0 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0), rect=None, special_flags=0) # give 255, 165, 0 for orange - https://www.pygame.org/docs/ref/color.html
        pygame.display.flip()

        dt = (AstroClock.tick(60) / 1000)

        #print(dt)
        #print(AstroClock.get_fps())


            
        




if __name__ == "__main__":
    main()
