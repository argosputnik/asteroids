import pygame
from constants import *
from circleshape import *
from player import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        screen.fill((0, 0, 0))  

        
        clock.tick(60)
        dt = clock.get_time() / 1000

        
        player.draw(screen)

        
        pygame.display.flip()


if __name__ == "__main__":
    main()
