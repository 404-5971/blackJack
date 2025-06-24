import pygame

from constants import *


def handle_window_events(fullscreen: bool) -> tuple[bool, bool]:
    """
    Handle pygame events.

    Args:
        fullscreen: Current fullscreen state

    Returns:
        Tuple of (should_continue_running, new_fullscreen_state)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, fullscreen
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            return True, not fullscreen

    return True, fullscreen


def toggle_fullscreen(is_fullscreen: bool) -> tuple[pygame.Surface, bool]:
    """
    Toggles between fullscreen and windowed mode.

    Args:
        is_fullscreen: Current fullscreen state

    Returns:
        Tuple of (new_screen_surface, new_fullscreen_state)
    """
    new_fullscreen_state: bool = not is_fullscreen

    if new_fullscreen_state:
        screen: pygame.Surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(
            (INITIAL_WIDTH, INITIAL_HEIGHT), pygame.RESIZABLE
        )

    return screen, new_fullscreen_state
