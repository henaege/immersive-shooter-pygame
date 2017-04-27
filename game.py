import pygame
from player import *
from game_functions import *
# core game loop
def run_game():
    # init pygame
    pygame.init()
    # set up a tuple for the screen size (horiz., vert.)
    screen_size = (1000, 800)
    # set up a tuple for the bg-color
    background_color = (82, 111, 53)
    # create a pygame screen to use
    screen = pygame.display.set_mode(screen_size)
    # set a caption on the terminal window
    pygame.display.set_caption("A Heroic 3rd-Person Shooter")
    the_player = Player(screen)
# Main game loop. Run forever or until break
    while 1:
        screen.fill(background_color)
        # the escape hatch from while
        check_events()

        # Draw the player
        the_player.draw_me()
        # clear the screen for the next time through the loop
        pygame.display.flip()


# Start the game!
run_game()
