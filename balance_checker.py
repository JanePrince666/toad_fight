import asyncio
import random
from frogs import BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog
from game import battle


async def check_balance():
    frog_classes = [BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog]
    balance_results = {}

    num_battles = 10000  # Количество боев для проверки баланса
    seeds = [42, 24, 99]  # Разные семена для рандомизации

    for frog_class in frog_classes:
        class_results = []

        for seed in seeds:
            wins = 0
            losses = 0

            random.seed(seed)  # Устанавливаем семя для рандомизации

            # Проведение боев против всех других классов
            for opponent_class in frog_classes:
                if frog_class != opponent_class:
                    results = await run_battles(num_battles, frog_class, opponent_class)
                    wins += results[1]  # Победы текущего класса
                    losses += results[2]  # Поражения текущего класса

            win_rate = wins / (wins + losses) if (wins + losses) > 0 else 0
            class_results.append({
                'wins': wins,
                'losses': losses,
                'win_rate': win_rate
            })

        balance_results[frog_class.__name__] = class_results

    return balance_results


async def run_battles(num_battles, frog_class1, frog_class2):
    results = {1: 0, 2: 0}

    for _ in range(num_battles):
        frog1 = frog_class1()
        frog2 = frog_class2()

        winner = await battle(frog1, frog2)
        results[winner] += 1

    return results


async def main():
    balance_results = await check_balance()
    for frog_name, results in balance_results.items():
        print(f"{frog_name}:")
        for i, result in enumerate(results):
            print(f"  Рандомизация {i+1}: Победы = {result['wins']}, Поражения = {result['losses']}, Уровень побед = {result['win_rate']:.2%}")

if __name__ == "__main__":
    asyncio.run(main())
