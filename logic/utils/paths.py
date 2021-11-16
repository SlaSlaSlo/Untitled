"""
Contains all paths to directories.
Paths start with "P_" and then the name of the file
"""

__all__ = [
    "P_DIR",
    "P_DATA",
    "P_CONFIG",
    "P_MAPS",
    "P_SAVES",
    "P_LOGIC",
    "P_UTILS",
    "P_RESOURCES",
    "P_FONTS",
    "P_IMAGES",
    "P_SOUNDS"
]

# Imports
from pathlib import Path

# Paths

P_DIR = Path().parent.parent.parent  # Main directory of the game

P_DATA = P_DIR / "data"
P_CONFIG = P_DATA / "config"
P_MAPS = P_DATA / "maps"
P_SAVES = P_DATA / "saves"

P_LOGIC = P_DIR / "logic"
P_UTILS = P_LOGIC / "utils"

P_RESOURCES = P_DIR / "resources"
P_FONTS = P_RESOURCES / "fonts"
P_IMAGES = P_RESOURCES / "images"
P_SOUNDS = P_RESOURCES / "sounds"
