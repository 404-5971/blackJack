import pygame
from pygame.key import ScancodeWrapper

from constants import *

# Global key states to track key presses across function calls
_key_states: dict[int, bool] = {
    pygame.K_UP: False,
    pygame.K_DOWN: False,
    pygame.K_j: False,
    pygame.K_k: False,
    pygame.K_RETURN: False,
}


class MainMenuButtonRects:
    """
    Class to store the menu buttons rects.
    rect1: Single Player button rect
    rect2: Multiplayer button rect
    rect3: Settings button rect
    rect4: Quit button rect
    """

    def __init__(
        self,
        rect1: pygame.Rect,
        rect2: pygame.Rect,
        rect3: pygame.Rect,
        rect4: pygame.Rect,
    ):
        if not all(
            isinstance(r, pygame.Rect)
            for r in [
                rect1,
                rect2,
                rect3,
                rect4,
            ]
        ):
            raise TypeError("All arguments must be pygame.Rect objects.")
        self.single_player_button_rect = rect1
        self.multiplayer_button_rect = rect2
        self.settings_button_rect = rect3
        self.quit_button_rect = rect4


def update_main_menu_button_rects(screen: pygame.Surface) -> MainMenuButtonRects:
    """
    Create a main menu button rects object.
    """
    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    # Calculate button dimensions (1/10 of screen height, 16:9 aspect ratio)
    button_height: int = screen_height // 5
    button_width: int = int(button_height * 16 / 9)

    fourth_of_screen_height: int = screen_height // 4
    offset: int = (fourth_of_screen_height - button_height) // 2

    # Draw buttons - center each button in its respective third
    # First third (top)
    single_player_button_x: int = (screen_width - button_width) // 2
    single_player_button_y: int = offset
    single_player_button_rect: pygame.Rect = pygame.Rect(
        single_player_button_x, single_player_button_y, button_width, button_height
    )

    # Second third (middle top)
    multiplayer_button_x: int = (screen_width - button_width) // 2
    multiplayer_button_y: int = fourth_of_screen_height + offset
    multiplayer_button_rect: pygame.Rect = pygame.Rect(
        multiplayer_button_x, multiplayer_button_y, button_width, button_height
    )

    # Third third (middle bottom)
    settings_button_x: int = (screen_width - button_width) // 2
    settings_button_y: int = fourth_of_screen_height * 2 + offset
    settings_button_rect: pygame.Rect = pygame.Rect(
        settings_button_x, settings_button_y, button_width, button_height
    )

    # Fourth third (bottom)
    quit_button_x: int = (screen_width - button_width) // 2
    quit_button_y: int = fourth_of_screen_height * 3 + offset
    quit_button_rect: pygame.Rect = pygame.Rect(
        quit_button_x, quit_button_y, button_width, button_height
    )

    return MainMenuButtonRects(
        single_player_button_rect,
        multiplayer_button_rect,
        settings_button_rect,
        quit_button_rect,
    )


def handle_main_menu_events(
    states: dict[str, bool],
    screen: pygame.Surface,
    pointer_pos: int,
) -> tuple[dict[str, bool], MainMenuButtonRects, int]:
    """
    Handle main menu events. \n
    Returns tuple[dict[str, bool], MainMenu]:
    - states: dict[str, bool]
    - main_menu_obj: MainMenu
    """

    global _key_states

    # Create main menu object
    main_menu_obj: MainMenuButtonRects = update_main_menu_button_rects(screen)

    def move_pointer(pointer_pos: int, direction: str) -> int:
        if direction == "up":
            if pointer_pos > 0:
                pointer_pos -= 1
            else:
                pointer_pos = 3
            return pointer_pos
        elif direction == "down":
            if pointer_pos < 3:
                pointer_pos += 1
            else:
                pointer_pos = 0
            return pointer_pos
        else:
            raise ValueError("Direction must be 'up' or 'down'.")

    keys: ScancodeWrapper = pygame.key.get_pressed()

    # Up arrow
    if keys[pygame.K_UP] and not _key_states[pygame.K_UP]:
        _key_states[pygame.K_UP] = True
        pointer_pos = move_pointer(pointer_pos, "up")

    # Down arrow
    elif keys[pygame.K_DOWN] and not _key_states[pygame.K_DOWN]:
        _key_states[pygame.K_DOWN] = True
        pointer_pos = move_pointer(pointer_pos, "down")

    # j (vim down)
    elif keys[pygame.K_j] and not _key_states[pygame.K_j]:
        _key_states[pygame.K_j] = True
        pointer_pos = move_pointer(pointer_pos, "down")

    # k (vim up)
    elif keys[pygame.K_k] and not _key_states[pygame.K_k]:
        _key_states[pygame.K_k] = True
        pointer_pos = move_pointer(pointer_pos, "up")

    # enter / return
    elif keys[pygame.K_RETURN] and not _key_states[pygame.K_RETURN]:
        _key_states[pygame.K_RETURN] = True
        match pointer_pos:
            case 0:
                states["main_menu"] = False
                states["single_player"] = True
            case 1:
                states["main_menu"] = False
                states["multiplayer"] = True
            case 2:
                states["main_menu"] = False
                states["settings"] = True
            case 3:
                states["main_menu"] = False
                states["quit"] = True
            case _:
                raise ValueError("Pointer position must be 0, 1, 2, or 3.")

    _key_states[pygame.K_UP] = keys[pygame.K_UP]
    _key_states[pygame.K_DOWN] = keys[pygame.K_DOWN]
    _key_states[pygame.K_j] = keys[pygame.K_j]
    _key_states[pygame.K_k] = keys[pygame.K_k]
    _key_states[pygame.K_RETURN] = keys[pygame.K_RETURN]

    if pygame.mouse.get_pressed()[0]:
        if main_menu_obj.single_player_button_rect.collidepoint(pygame.mouse.get_pos()):
            states["main_menu"] = False
            states["single_player"] = True
        elif main_menu_obj.multiplayer_button_rect.collidepoint(pygame.mouse.get_pos()):
            states["main_menu"] = False
            states["multiplayer"] = True
        elif main_menu_obj.settings_button_rect.collidepoint(pygame.mouse.get_pos()):
            states["main_menu"] = False
            states["settings"] = True
        elif main_menu_obj.quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            states["main_menu"] = False
            states["quit"] = True

    return states, main_menu_obj, pointer_pos


def draw_main_menu(
    screen: pygame.Surface,
    main_menu_button_rects_obj: MainMenuButtonRects,
    pointer_pos: int,
) -> None:
    """
    Draw the main menu.
    """

    buttonFont: pygame.font.Font = pygame.font.SysFont(
        "DejaVu Sans", main_menu_button_rects_obj.single_player_button_rect.width // 7
    )

    # First (top)
    single_player_button_text: pygame.Surface = buttonFont.render(
        "Single Player", True, COLOR_BUTTON_TEXT
    )
    single_player_button_text_rect: pygame.Rect = single_player_button_text.get_rect()
    single_player_button_text_rect.center = (
        main_menu_button_rects_obj.single_player_button_rect.x
        + main_menu_button_rects_obj.single_player_button_rect.width // 2,
        main_menu_button_rects_obj.single_player_button_rect.y
        + main_menu_button_rects_obj.single_player_button_rect.height // 2,
    )
    pygame.draw.rect(
        screen, COLOR_BUTTON, main_menu_button_rects_obj.single_player_button_rect
    )  # Gray button
    pygame.draw.rect(
        screen, COLOR_BUTTON_HOVER, main_menu_button_rects_obj.single_player_button_rect, 2
    )  # White border
    screen.blit(single_player_button_text, single_player_button_text_rect)

    # Second (middle top)
    multiplayer_button_text: pygame.Surface = buttonFont.render(
        "Multiplayer", True, COLOR_BUTTON_TEXT
    )
    multiplayer_button_text_rect: pygame.Rect = multiplayer_button_text.get_rect()
    multiplayer_button_text_rect.center = (
        main_menu_button_rects_obj.multiplayer_button_rect.x
        + main_menu_button_rects_obj.multiplayer_button_rect.width // 2,
        main_menu_button_rects_obj.multiplayer_button_rect.y
        + main_menu_button_rects_obj.multiplayer_button_rect.height // 2,
    )
    pygame.draw.rect(
        screen, COLOR_BUTTON, main_menu_button_rects_obj.multiplayer_button_rect
    )  # Gray button
    pygame.draw.rect(
        screen, COLOR_BUTTON_HOVER, main_menu_button_rects_obj.multiplayer_button_rect, 2
    )  # White border
    screen.blit(multiplayer_button_text, multiplayer_button_text_rect)

    # Third (middle bottom)
    settings_button_text: pygame.Surface = buttonFont.render(
        "Settings", True, COLOR_BUTTON_TEXT
    )
    settings_button_text_rect: pygame.Rect = settings_button_text.get_rect()
    settings_button_text_rect.center = (
        main_menu_button_rects_obj.settings_button_rect.x
        + main_menu_button_rects_obj.settings_button_rect.width // 2,
        main_menu_button_rects_obj.settings_button_rect.y
        + main_menu_button_rects_obj.settings_button_rect.height // 2,
    )
    pygame.draw.rect(
        screen, COLOR_BUTTON, main_menu_button_rects_obj.settings_button_rect
    )  # Gray button
    pygame.draw.rect(
        screen, COLOR_BUTTON_HOVER, main_menu_button_rects_obj.settings_button_rect, 2
    )  # White border
    screen.blit(settings_button_text, settings_button_text_rect)

    # Fourth (bottom)
    quit_button_text: pygame.Surface = buttonFont.render(
        "Quit", True, COLOR_BUTTON_TEXT
    )
    quit_button_text_rect: pygame.Rect = quit_button_text.get_rect()
    quit_button_text_rect.center = (
        main_menu_button_rects_obj.quit_button_rect.x + main_menu_button_rects_obj.quit_button_rect.width // 2,
        main_menu_button_rects_obj.quit_button_rect.y + main_menu_button_rects_obj.quit_button_rect.height // 2,
    )
    pygame.draw.rect(
        screen, COLOR_BUTTON, main_menu_button_rects_obj.quit_button_rect
    )  # Gray button
    pygame.draw.rect(
        screen, COLOR_BUTTON_HOVER, main_menu_button_rects_obj.quit_button_rect, 2
    )  # White border
    screen.blit(quit_button_text, quit_button_text_rect)

    def draw_pointer(button_rect: pygame.Rect) -> tuple[pygame.Surface, pygame.Rect]:
        pointer_width: int = button_rect.width // 3
        pointer_height: int = button_rect.height // 3
        pointer_x: int = int(button_rect.x - pointer_width * 1.1)
        pointer_y: int = button_rect.y + button_rect.height // 2 - pointer_height // 2
        pointer_surface: pygame.Surface = pygame.Surface(
            (pointer_width, pointer_height), pygame.SRCALPHA
        )
        pygame.draw.polygon(
            pointer_surface,
            COLOR_BUTTON_HOVER,
            [(0, 0), (pointer_width, pointer_height // 2), (0, pointer_height)],
        )
        pointer_rect: pygame.Rect = pointer_surface.get_rect(
            center=(pointer_x + pointer_width // 2, pointer_y + pointer_height // 2)
        )
        return pointer_surface, pointer_rect

    # Draw pointer. The pointer will be a triangle that points to the selected button.
    match pointer_pos:
        case 0:
            pointer_surface, pointer_rect = draw_pointer(
                main_menu_button_rects_obj.single_player_button_rect
            )
        case 1:
            pointer_surface, pointer_rect = draw_pointer(
                main_menu_button_rects_obj.multiplayer_button_rect
            )
        case 2:
            pointer_surface, pointer_rect = draw_pointer(
                main_menu_button_rects_obj.settings_button_rect
            )
        case 3:
            pointer_surface, pointer_rect = draw_pointer(main_menu_button_rects_obj.quit_button_rect)
        case _:
            raise ValueError("Pointer position must be 0, 1, 2, or 3.")

    screen.blit(pointer_surface, pointer_rect)
