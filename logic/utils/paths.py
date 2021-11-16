"""
Contains all paths to directories.
Paths start with "P_" and then the name of the file
"""

__all__ = [
    "DIR",
    "P_DATA",
    "P_CONFIG",
    "P_MAPS",
    "P_SAVES",
    "P_LOGIC",
    "P_UTILS"
]

# Imports
from pathlib import Path

# Paths

DIR = Path().parent.parent.parent  # Main directory of the game

P_DATA = DIR / "data"
P_CONFIG = P_DATA / "config"
P_MAPS = P_DATA / "maps"
P_SAVES = P_DATA / "saves"

P_LOGIC = DIR / "logic"
P_UTILS = P_LOGIC / "utils"
