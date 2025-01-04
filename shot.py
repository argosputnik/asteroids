import pygame
from circleshape import *
from groups import asteroids, updateable, drawable

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
     
    def update(self, dt):
        self.position += self.velocity * dt



