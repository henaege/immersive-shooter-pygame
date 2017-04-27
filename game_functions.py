import pygame
import sys

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                # the user clicked the red x. Get out of loop and exit game
            sys.exit()
            