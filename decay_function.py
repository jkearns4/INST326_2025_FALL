
def apply_daily_decay(stats):
    """
    Applies daily stat decay for hunger and thirst only.
    """

    decay = {"hunger": 10, "thirst": 12}

    for stat, amount in decay.items():
        stats[stat] -= amount

        if stats[stat] <= 0:
            stats[stat] = 0
            stats["health"] -= 10  # health penalty for starvation/dehydration

    return stats

fake_stats = {
    "health": 100,
    "energy": 100,
    "hunger": 50,
    "thirst": 50
}

updated_stats = apply_daily_decay(fake_stats)
print(updated_stats)
