from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS == self.radius:
            return
        
        ramdomAngle = random.uniform(20,50)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        newVelocity = self.velocity * ASTEROIDS_BOOST
        vec1 =  self.velocity.rotate(ramdomAngle)
        vec2 =  self.velocity.rotate(-ramdomAngle)


        self.spawn(newRadius,(self.position), newVelocity +vec2)
        self.spawn(newRadius,(self.position), newVelocity +vec1)



    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.position += dt * self.velocity


    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius,2)