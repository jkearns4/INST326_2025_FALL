import json
import random


# Load all game data from JSON


def load_config(path):
   """
   Primary author: Kenneth Kong
   Techniques claimed: with statement, json.load()


   Load game configuration data from a JSON file.


   Parameters:
       path (str): Path to the JSON configuration file.


   Returns:
       dict: Parsed configuration dictionary containing starting stats,
             decay values, action outcomes, events, and max_days.
   """
   with open(path, "r", encoding="utf-8") as f:
       return json.load(f)