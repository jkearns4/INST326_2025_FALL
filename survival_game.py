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

class Player:
   """
   Primary author: Josh Harris

   Represents the player character and survival-related stats.
   """


   def __init__(self, health, energy, hunger, thirst, shelter):
       """
       Primary author: Josh Harris
        Initialize a new Player object.


       Parameters:
           health (int): Starting health value.
           energy (int): Starting energy value.
           hunger (int): Starting hunger value.
           thirst (int): Starting thirst value.
           shelter (int): Starting shelter level.
       """


       self.health = health
       self.energy = energy
       self.hunger = hunger
       self.thirst = thirst
       self.shelter = shelter

 def apply_changes(self, changes):
       """
       Primary author: Josh Harris


       Apply stat changes from an action or an event.


       Parameters:
           changes (dict): Mapping from stat name (str) to an integer delta.


       Returns:
           None
       """
       for stat, delta in changes.items():
           if hasattr(self, stat):
               value = getattr(self, stat) + delta
               setattr(self, stat, max(value, 0))


       if self.health <= 0:
           self.health = 0

def apply_decay(self, decay):
       """
       Primary author: Josh Harris


       Apply daily decay to hunger and thirst and penalize health if either
       reaches zero.


       Parameters:
           decay (dict): Mapping from stat name (str) to an integer amount
                         that is subtracted each day.


       Returns:
           None
       """
       for stat, amount in decay.items():
           value = getattr(self, stat) - amount
           if value <= 0:
               setattr(self, stat, 0)
               self.health -= 10
           else:
               setattr(self, stat, value)


       if self.health < 0:
           self.health = 0

 def is_alive(self):
       """
       Primary author: Josh Harris


       Check if the player is still alive.


       Returns:
           bool: True if health is greater than zero, False otherwise.
       """
       return self.health > 0





# Action Outcome System

def get_action_outcome(action, outcome_table):
   """
   Primary author: Kenneth Kong


   Roll a 1–20 value and choose an outcome tier for the given action.


   Parameters:
       action (str): The action name (key in outcome_table).
       outcome_table (dict): Mapping from action names to a list of outcome
                             tiers. Each tier is a list or tuple in the form
                             [result_label, severity, stat_changes_dict].


   Returns:
       dict: Dictionary with keys:
             - "result" (str): label of the outcome.
             - "severity" (int): relative impact of the outcome.
             - "changes" (dict): stat changes for the outcome.
   """
   roll = random.randint(1, 20)
   tiers = outcome_table[action]


   if roll >= 17:
       tier = tiers[0]
   elif roll >= 12:
       tier = tiers[1]
   elif roll >= 6:
       tier = tiers[2]
   else:
       tier = tiers[3]


   return {
       "result": tier[0],
       "severity": tier[1],
       "changes": tier[2]
   }



# Random Event Algorithm

def trigger_random_event(events, player):
   """
   Primary author: Kenneth Kong


   Possibly trigger a random event for the current day. Each event stores
   a base chance, which is reduced by the player's shelter level.


   Parameters:
       events (list[dict]): List of event dictionaries. Each event should
                            define "name", "description", "base_chance",
                            and "effects" (stat changes).
       player (Player): The active Player object.


   Returns:
       dict | None: The event dictionary that occurred, or None if no
                    event was triggered.
   """
   for event in events:
       chance = event["base_chance"]
       adjusted = max(0, chance - (player.shelter * 0.03))
       roll = random.random()


       if roll < adjusted:
           player.apply_changes(event["effects"])
           return event


   return None

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




