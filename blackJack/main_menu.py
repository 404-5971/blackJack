import pygame

from constants import *


def draw_main_menu(
    screen: pygame.Surface,
) -> dict[str, pygame.Rect]:
    """
    Draw the main menu.
    """

    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    # Calculate button dimensions (1/10 of screen height, 16:9 aspect ratio)
    button_height: int = screen_height // 5
    button_width: int = int(button_height * 16 / 9)

    third_of_screen_height: int = screen_height // 3
    offset: int = (third_of_screen_height - button_height) // 2

    buttonFont: pygame.font.Font = pygame.font.SysFont("DejaVu Sans", button_width // 7)

    # Draw buttons - center each button in its respective third
    # First third (top)
    single_player_button_x: int = (screen_width - button_width) // 2
    single_player_button_y: int = offset
    single_player_button_rect: pygame.Rect = pygame.Rect(
        single_player_button_x, single_player_button_y, button_width, button_height
    )
    single_player_button_text: pygame.Surface = buttonFont.render(
        "Single Player", True, COLOR_BUTTON_TEXT
    )
    single_player_button_text_rect: pygame.Rect = single_player_button_text.get_rect()
    single_player_button_text_rect.center = (
        single_player_button_x + button_width // 2,
        single_player_button_y + button_height // 2,
    )
    pygame.draw.rect(screen, COLOR_BUTTON, single_player_button_rect)  # Gray button
    pygame.draw.rect(
        screen, COLOR_BUTTON_HOVER, single_player_button_rect, 2
    )  # White border
    screen.blit(single_player_button_text, single_player_button_text_rect)

    # Second third (middle)
    multiplayer_button_x: int = (screen_width - button_width) // 2
    multiplayer_button_y: int = third_of_screen_height + offset
    multiplayer_button_rect: pygame.Rect = pygame.Rect(
        multiplayer_button_x, multiplayer_button_y, button_width, button_height
    )
    multiplayer_button_text: pygame.Surface = buttonFont.render(
        "Multiplayer", True, COLOR_BUTTON_TEXT
    )
    multiplayer_button_text_rect: pygame.Rect = multiplayer_button_text.get_rect()
    multiplayer_button_text_rect.center = (
        multiplayer_button_x + button_width // 2,
        multiplayer_button_y + button_height // 2,
    )
    pygame.draw.rect(screen, COLOR_BUTTON, multiplayer_button_rect)  # Gray button
    pygame.draw.rect(
        screen, COLOR_BUTTON_HOVER, multiplayer_button_rect, 2
    )  # White border
    screen.blit(multiplayer_button_text, multiplayer_button_text_rect)

    # Third third (bottom)
    settings_button_x: int = (screen_width - button_width) // 2
    settings_button_y: int = third_of_screen_height * 2 + offset
    settings_button_rect: pygame.Rect = pygame.Rect(
        settings_button_x, settings_button_y, button_width, button_height
    )
    settings_button_text: pygame.Surface = buttonFont.render(
        "Settings", True, COLOR_BUTTON_TEXT
    )
    settings_button_text_rect: pygame.Rect = settings_button_text.get_rect()
    settings_button_text_rect.center = (
        settings_button_x + button_width // 2,
        settings_button_y + button_height // 2,
    )
    pygame.draw.rect(screen, COLOR_BUTTON, settings_button_rect)  # Gray button
    pygame.draw.rect(
        screen, COLOR_BUTTON_HOVER, settings_button_rect, 2
    )  # White border
    screen.blit(settings_button_text, settings_button_text_rect)

    return {
        "single_player_button_rect": single_player_button_rect,
        "multiplayer_button_rect": multiplayer_button_rect,
        "settings_button_rect": settings_button_rect,
    }


def handle_main_menu_events(
    states: dict[str, bool],
    single_player_button_rect: pygame.Rect,
    multiplayer_button_rect: pygame.Rect,
    settings_button_rect: pygame.Rect,
) -> dict[str, bool]:
    """
    Handle main menu events.
    """
    if pygame.mouse.get_pressed()[0]:
        if single_player_button_rect.collidepoint(pygame.mouse.get_pos()):
            states["main_menu"] = False
            states["single_player"] = True
        elif multiplayer_button_rect.collidepoint(pygame.mouse.get_pos()):
            states["main_menu"] = False
            states["multiplayer"] = True
        elif settings_button_rect.collidepoint(pygame.mouse.get_pos()):
            states["main_menu"] = False
            states["settings"] = True

    return states
