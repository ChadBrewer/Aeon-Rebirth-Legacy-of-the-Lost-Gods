# src/__init__.py

# Importing key components to be used throughout the game
from .settings import Settings
from .main import Game
from .game.player import Player
from .game.enemy import Enemy
from .game.item import Item
from .utils.helpers import HelperFunctions
from .utils.constants import Constants

# Initialize game settings
settings = Settings()

# Initialize a game instance variable (optional, for later use across the game)
game_instance = None  # This will store the current game instance if needed

# Set up logging for the game (for debugging and error messages)
import logging
logging.basicConfig(level=logging.DEBUG)

# Global state or objects initialization
# Can be used to initialize any global variables you might need, such as a list of active players
game_objects = []
