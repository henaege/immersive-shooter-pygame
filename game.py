import pygame
from player import *
from game_functions import *
from enemy import *
from pygame.sprite import *
# core game loop
def run_game():
    # init pygame
    pygame.init()
    # set up a tuple for the screen size (horiz., vert.)
    screen_size = (1200, 609)
    # set up a tuple for the bg-color
    # background_color = (82, 111, 53)
    background_image = pygame.image.load('./images/background.jpg')

    # create a pygame screen to use
    screen = pygame.display.set_mode(screen_size)
    # set a caption on the terminal window
    pygame.display.set_caption("A Heroic 3rd-Person Shooter")
    the_player = Player(screen, './images/new.png', 100, 250)
    bad_guy = Enemy(screen)
    the_player_group = Group()
    the_player_group.add(the_player)
    enemies = Group()
    enemies.add(bad_guy)

# Main game loop. Run forever or until break
    while 1:
        # screen.fill(background_color)
        # the escape hatch from while
        check_events(the_player)
        # Drew the background
        screen.blit(background_image, (0,0))
        # Draw the player
        for player in the_player_group:
            the_player.draw_me()

        # Draw and update the bad guy   
        bad_guy.draw_me()
        bad_guy.update_me(the_player)

        hero_died = groupcollide(the_player_group, enemies, True, False)
        print hero_died

        # clear the screen for the next time through the loop
        pygame.display.flip()


# Start the game!
run_game()
