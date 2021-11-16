"""
Used to read files
"""

__all__ = [
    "DATA"
]

# Imports
from json import load as json_load
from os import listdir
from .paths import *
from .exceptions import *


def read_file(f_dir, f_name):  # Read the given file in the given directory
    if f_name.endswith(".json"):
        f = open(f_dir / f_name)
        name = f_name.replace(".json", "").upper()
        if name in LOADED:
            raise FileAlreadyLoaded(f"The file {f_name} was already loaded before.")

        LOADED[name] = json_load(f)


def read_dirs(dirs):  # Read all files in the given directories
    for i in dirs:
        for j in listdir(i):
            read_file(i, j)


LOADED = {}
# Read directories and files
read_dirs([P_CONFIG, P_MAPS, P_SAVES])
...

DATA = LOADED
