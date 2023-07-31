import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Intialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, sceen, ship)

run_game()

