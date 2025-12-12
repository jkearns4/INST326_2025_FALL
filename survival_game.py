import json
import random


# Load all game data from JSON


def load_config(path):
   """
   Primary author: Kenneth Kong

   Load game configuration data from a JSON file.

   Parameters:
       path (str): Path to the JSON configuration file.

   Returns:
       dict: Parsed configuration dictionary containing starting stats,
             decay values, action outcomes, events, and max_days.
   """
   with open(path, "r", encoding="utf-8") as f:
       return json.load(f)






class Game:
   """
   Primary author: Jason Kearns


   Manages the overall game state and main game loop.
   """


   def __init__(self, config):
       """
       Primary author: Jason Kearns




       Initialize the game using configuration data.


       Parameters:
           config (dict): Configuration dictionary loaded from JSON. It should
                          contain keys "starting_stats", "daily_decay",
                          "action_outcomes", "events", and "max_days".
       """
       stats = config["starting_stats"]
       self.player = Player(
           stats["health"],
           stats["energy"],
           stats["hunger"],
           stats["thirst"],
           stats["shelter"]
       )


       self.decay = config["daily_decay"]
       self.actions = config["action_outcomes"]
       self.events = config["events"]
       self.max_days = config["max_days"]
       self.day = 1


   def choose_action(self):
       """
       Primary author: Jason Kearns




       Prompt the user to choose an action for the day and validate input.


       Returns:
           str: The action name chosen by the user.
       """
       # list comprehension to build the list of valid actions
       valid = [action_name for action_name in self.actions.keys()]
       print("\nActions:", ", ".join(valid))


       while True:
           choice = input("Choose an action: ").strip().lower()
           if choice in valid:
               return choice
           print("Invalid action. Try again.")
