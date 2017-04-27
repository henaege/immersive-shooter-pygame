import pygame
import sys


def check_events(the_player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                # the user clicked the red x. Get out of loop and exit game
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("User pressed up")
                the_player.should_move('up', True)
            elif event.key == pygame.K_DOWN:
                print("User pressed down")
                the_player.should_move('down', True)
            elif event.key == pygame.K_LEFT:
                print("User pressed left")
                the_player.should_move('left', True)
            elif event.key == pygame.K_RIGHT:
                print("User pressed right")
                the_player.should_move('right', True)
            elif event.key == pygame.K_SPACE:
                keys_pressed['space'] = True
                # Shoot
        elif event.type == pygame.KEYUP:
            print "The user let go of the key"
            if event.key == pygame.K_UP:
                the_player.should_move('up', False)
            if event.key == pygame.K_DOWN:
                the_player.should_move('down', False)
            if event.key == pygame.K_LEFT:
                the_player.should_move('left', False)
            if event.key == pygame.K_RIGHT:
                the_player.should_move('right', False)
