def player_daily_decisions(player_stats, decision_outcome):

    """
    This function provides the user with choices each day in the game, takes the input of their decision, and processes it, applying changes to the player stats and printing the results.

    Parameters:
        player_stats (dict): This is a dictionary that contains the stats of the player.
        decision_outcome (function): This is a function that takes the player decision as the input and returns a dictionary with keys:
                                    "result" (str): What the outcome is.
                                    "severity" (int): What the severity is as a number.
                                    "stat_changes" (dict): A dictionary of the changes to the player stats.

        returns:
            tuple:
                updated_stats (dict): The player's updated stats after the affects of their decisions have taken place.
                outcome (dict): The outcome of their decision; includes stat_changes.
    """

    accepted_decisions = ["hunt", "search_food", "rest", "build_shelter"]

    print(f"What action would you like to take today? Your options are: {', '.join(accepted_decisions)}")
    
    
    while True:
        decision_input = input("Enter your decision: ").strip().lower()
        if decision_input in accepted_decisions:
            break
        print("Decision not an accepted input. Please enter another decision.")
        

    outcome = decision_outcome(decision_input)
    
    for stat, change in outcome["stat_changes"].items():
        if stat in player_stats:
            player_stats[stat] += change

    player_stats = apply_daily_decay(player_stats)

    print(f"Outcome: {outcome['result']}, Stat Changes: {outcome['stat_changes']}")
    print(f"Updated Stats: {player_stats}")
    
    return player_stats, outcome

