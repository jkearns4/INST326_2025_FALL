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


def run_day(self):
       """
       Primary author: Kenneth Kong


       Run the full logic for a single in-game day:
       - Show current stats
       - Prompt for an action
       - Apply the action outcome
       - Apply daily decay
       - Possibly trigger a random event
       - Check for player death


       Returns:
           bool: True if the player survives the day, False if the player dies.
       """
       print(f"\n--- Day {self.day} ---")
       print(self.player)


       action = self.choose_action()
       outcome = get_action_outcome(action, self.actions)


       print(f"\nOutcome: {outcome['result'].replace('_', ' ').title()}")
       print("Stat changes from action:", outcome["changes"])


       # Copy the changes so we can adjust them for hunger/food handling
       changes = dict(outcome["changes"])
       if "food" in changes:
           food_val = changes.pop("food")
           changes["hunger"] = changes.get("hunger", 0) - food_val


       self.player.apply_changes(changes)
       self.player.apply_decay(self.decay)


       event = trigger_random_event(self.events, self.player)
       if event:
           print(f"\nEVENT: {event['name']}")
           print(event["description"])
           print("Event effects:", event["effects"])


       if not self.player.is_alive():
           print("\nYou died. Game over.")
           return False


       return True


   
   def run(self):
       """
       Primary author: Jason Kearns


       Run the full game loop from day 1 until the player either dies
       or survives the maximum number of days.


       Returns:
           None
       """
       print("\nWelcome to SURVIVAL.")
       print("Try to live through all days in a zombie-infested city.\n")


       while self.day <= self.max_days:
           alive = self.run_day()
           if not alive:
               return


           self.day += 1


       print("\nYou survived all days. You win!")


# Main entry point

if __name__ == "__main__":
   # Primary author: Kenneth Kong
   config = load_config("survival_config.json")
   game = Game(config)
   game.run()




