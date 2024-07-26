import asyncio
import random
from frogs import BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog
from game import battle


async def check_balance():
    """
    Checks the balance of different frog classes by running a series of battles.

    Returns:
        dict: A dictionary containing the results of battles for each frog class,
              including wins, losses, and win rates.
    """
    frog_classes = [BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog]
    balance_results = {}

    num_battles = 10000  # Number of battles to check balance

    for frog_class in frog_classes:
        class_results = []

        wins = 0
        losses = 0

        # Conduct battles against all other classes
        for opponent_class in frog_classes:
            if frog_class != opponent_class:
                results = await run_battles(num_battles, frog_class, opponent_class)
                wins += results[1]  # Wins for the current class
                losses += results[2]  # Losses for the current class

        # Calculate win rate
        win_rate = wins / (wins + losses) if (wins + losses) > 0 else 0
        class_results.append({
            'wins': wins,
            'losses': losses,
            'win_rate': win_rate
        })

        balance_results[frog_class.__name__] = class_results

    return balance_results


async def run_battles(num_battles, frog_class1, frog_class2):
    """
    Runs a specified number of battles between two frog classes.

    Args:
        num_battles (int): The number of battles to run.
        frog_class1 (Frog): The first frog class.
        frog_class2 (Frog): The second frog class.

    Returns:
        dict: A dictionary containing the results of the battles,
              with keys 1 and 2 representing the number of wins for each frog.
    """
    results = {1: 0, 2: 0}

    for _ in range(num_battles):
        frog1 = frog_class1()  # Create an instance of the first frog class
        frog2 = frog_class2()  # Create an instance of the second frog class

        # Determine the winner of the battle
        winner = await battle(frog1, frog2)
        results[winner] += 1

    return results


async def main():
    balance_results = await check_balance()
    for frog_name, results in balance_results.items():
        print(f"{frog_name}: Wins = {results[0]['wins']}, Losses = {results[0]['losses']}, Win Rate = {results[0]['win_rate']:.2%}")


if __name__ == "__main__":
    asyncio.run(main())
