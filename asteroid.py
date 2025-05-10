from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.center = [x, y]
        #self.radius = radius

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        # sub-classes must override

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rangle = random.uniform(20, 50)
            ast1 = self.velocity.rotate(rangle)
            ast2 = self.velocity.rotate(-rangle)
            new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid1 = Asteroid(self.position.x, self.position.y, new_ast_radius)
            Asteroid2 = Asteroid(self.position.x, self.position.y, new_ast_radius)
            Asteroid1.velocity = ast1 * 1.2
            Asteroid2.velocity = ast2 * 1.2

