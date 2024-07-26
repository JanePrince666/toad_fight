import asyncio
import random
from frogs import BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog


async def battle(frog1, frog2):
    """
    Simulates a battle between two frogs.

    Args:
        frog1 (Frog): The first frog participating in the battle.
        frog2 (Frog): The second frog participating in the battle.

    Returns:
        int: 1 if the first frog wins, 2 if the second frog wins.
    """
    # Determine who attacks first based on initiative
    number_one = frog1.get_initiative()
    number_two = frog2.get_initiative()

    # Resolve ties in initiative by re-rolling
    while number_one == number_two:
        number_one = frog1.get_initiative()
        number_two = frog2.get_initiative()

    # Assign first and second frogs based on initiative
    first_frog, second_frog = (frog1, frog2) if number_one > number_two else (frog2, frog1)

    # Continue the battle until one frog's health reaches zero
    while first_frog.health > 0 and second_frog.health > 0:
        damage_to_second = first_frog.get_damage() - second_frog.get_armor()

        # Apply damage to the second frog if the damage is positive
        if damage_to_second > 0:
            second_frog.health -= damage_to_second

        # Check if the second frog is defeated
        if second_frog.health <= 0:
            return 1  # First frog wins

        damage_to_first = second_frog.get_damage() - first_frog.get_armor()

        # Apply damage to the first frog if the damage is positive
        if damage_to_first > 0:
            first_frog.health -= damage_to_first

    return 2  # Second frog wins


async def run_battles(num_battles):
    """
    Runs a specified number of battles between randomly selected frogs.

    Args:
        num_battles (int): The number of battles to run.

    Returns:
        dict: A dictionary containing the results of the battles,
              with keys 1 and 2 representing the number of wins for each frog.
    """
    results = {1: 0, 2: 0}

    for fight in range(num_battles):
        # Randomly select two frogs for the battle
        frog_classes = [BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog]
        frog1 = random.choice(frog_classes)()
        frog2 = random.choice(frog_classes)()

        # Determine the winner of the battle
        winner = await battle(frog1, frog2)
        results[winner] += 1

    return results


async def main():
    num_battles = 100  # Specify the number of battles to run
    results1 = await run_battles(num_battles)
    results2 = await run_battles(num_battles)

    # Print the results of the battles to console
    print(f"First frog wins: {results1[1] + results2[1]}")
    print(f"Second frog wins: {results1[2] + results2[1]}")


if __name__ == "__main__":
    asyncio.run(main())
