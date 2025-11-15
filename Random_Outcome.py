import random

def random_outcome(action):
    """
    Generates a random outcome for a player's action using a simplified DnD-style system.
    Each action has different possible results and different levels of severity.
    
    Parameters:
        action (str): the action the player chose ("hunt", "search_food", "rest", etc.)
    
    Returns:
        dict: outcome information, including:
            - "result": the label of the outcome (success, fail, injury, etc.)
            - "severity": a number describing how good or bad it was
            - "stat_changes": a dictionary of stat adjustments
    """

    # Define possible outcomes for each action
    outcome_table = {
        "hunt": [
            ("great_success", 5, {"food": +4, "energy": -3, "health": 0}),
            ("success", 3, {"food": +2, "energy": -3, "health": 0}),
            ("fail", 2, {"food": 0, "energy": -2, "health": 0}),
            ("injury", 1, {"food": 0, "energy": -2, "health": -3})
        ],
        "search_food": [
            ("success", 4, {"food": +1, "energy": -1, "health": 0}),
            ("small_success", 3, {"food": +1, "energy": -1, "health": 0}),
            ("fail", 2, {"food": 0, "energy": -1, "health": 0}),
            ("spoiled_food", 1, {"food": +1, "energy": -1, "health": -2})
        ],
        "rest": [
            ("good_rest", 4, {"energy": +2, "hunger": +1, "thirst": +1}),
            ("neutral_rest", 3, {"energy": +1, "hunger": +1, "thirst": +1}),
            ("poor_rest", 2, {"energy": 0, "hunger": +1, "thirst": +1})
        ]
    }

    # Get the possible outcomes for the selected action
    if action not in outcome_table:
        return {"result": "invalid_action", "severity": 0, "stat_changes": {}}

    outcomes = outcome_table[action]

    # Roll a random outcome 
    roll = random.randint(1, 20)

    # Pick a result based on the roll
    # higher rolls = better outcomes
    if roll >= 17:
        result, severity, changes = outcomes[0]
    elif roll >= 12:
        result, severity, changes = outcomes[1]
    elif roll >= 6:
        result, severity, changes = outcomes[2]
    else:
        result, severity, changes = outcomes[3]

    # Return all outcome information
    return {
        "result": result,
        "severity": severity,
        "stat_changes": changes
    }
