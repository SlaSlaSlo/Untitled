"""
Contains general utility functions
"""

__all__ = [
    "load_image",
    "scale_surf",
    "rotate_surf",
    "clip"
]

import pygame
from .paths import *


def load_image(name, scale=1, alpha=False):
    """loads an image"""
    image = pygame.image.load(P_RESOURCES / f"{name}.png")
    if scale != 1:
        image = scale_surf(image, scale)
    if alpha:
        return image.convert_alpha()
    return image.convert()


def scale_surf(surf, scale):
    """Scales a surface by amount 'scale'"""
    return pygame.transform.scale(surf, (int(surf.get_width() * scale), int(surf.get_height() * scale)))


def rotate_surf(surf, angle) -> pygame.surface.Surface:
    """Rotates a surface"""
    return pygame.transform.rotate(surf, angle)


def clip(surf: pygame.surface.Surface, rect: pygame.rect.Rect):
    """Clips a surf out of another surf"""
    handle_surf = surf.copy()
    handle_surf.set_clip(rect)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def clamp(value: float, mini: float, maxi: float) -> float:
    """Claps value between mini and maxi"""
    if value < mini:
        return mini
    elif value > maxi:
        return maxi
    return value
