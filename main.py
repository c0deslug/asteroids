# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    AstroClock = pygame.time.Clock()
    PlayerShip = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)

    dt = 0 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        PlayerShip.update(dt)    
        screen.fill((0, 0, 0), rect=None, special_flags=0) # give 255, 165, 0 for orange - https://www.pygame.org/docs/ref/color.html
        PlayerShip.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = (AstroClock.tick(60) / 1000)
        
        #print(dt)
        #print(AstroClock.get_fps())


            
        




if __name__ == "__main__":
    main()
