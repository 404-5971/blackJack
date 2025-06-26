import pygame
import sys

from constants import *
from helpers import *
from main_menu import *


def main() -> None:
    """Main game function."""
    pygame.init()

    screen: pygame.Surface = pygame.display.set_mode(
        (INITIAL_WIDTH, INITIAL_HEIGHT), pygame.RESIZABLE
    )
    pygame.display.set_caption("Resizable Grid (Press F11 for Fullscreen)")

    fullscreen: bool = False
    running: bool = True
    clock: pygame.time.Clock = pygame.time.Clock()

    states: dict[str, bool] = {
        "main_menu": True,
        "single_player": False,
        "multiplayer": False,
        "settings": False,
    }

    pointer_pos: int = 0

    while running:
        # Handle events
        new_fullscreen: bool
        running, new_fullscreen = handle_window_events(fullscreen)

        # Update screen mode if needed
        if new_fullscreen != fullscreen:
            screen, fullscreen = toggle_fullscreen(fullscreen)

        screen.fill(COLOR_BACKGROUND)

        # Render
        match states:
            case {"main_menu": True}:
                states, main_menu_obj, pointer_pos = handle_main_menu_events(
                    states, screen, pointer_pos
                )
                draw_main_menu(screen, main_menu_obj, pointer_pos)
            case {"single_player": True}:
                print("single_player")
                # draw_single_player(screen)
                # states = handle_single_player_events(states)
                pass
            case {"multiplayer": True}:
                print("multiplayer")
                # draw_multiplayer(screen)
                # states = handle_multiplayer_events(states)
                pass
            case {"settings": True}:
                print("settings")
                # draw_settings(screen)
                # states = handle_settings_events(states)
                pass

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
