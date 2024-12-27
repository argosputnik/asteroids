import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    #print("Starting asteroids!")
    #print("Screen width: " + str(SCREEN_WIDTH))
    #print("Screen height: " +  str(SCREEN_HEIGHT))

    run = True
    while run == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


    # This should be at the same level as the function definition
if __name__ == "__main__":
    main()


