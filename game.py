import asyncio
import random
from frogs import BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog


async def battle(frog1, frog2):
    # Определяем, кто атакует первым на основе инициативы
    number_one = frog1.get_initiative()
    number_two = frog2.get_initiative()
    while number_one == number_two:
        number_one = frog1.get_initiative()
        number_two = frog2.get_initiative()
        # Определяем, кто атакует первым на основе инициативы
    first_frog, second_frog = (frog1, frog2) if number_one > number_two else (frog2, frog1)
    while first_frog.health > 0 and second_frog.health > 0:
        damage_to_second = first_frog.get_damage() - second_frog.get_armor()
        if damage_to_second > 0:
            second_frog.health -= damage_to_second

        if second_frog.health <= 0:
            return 1  # Победа первой жабы

        damage_to_first = second_frog.get_damage() - first_frog.get_armor()
        if damage_to_first > 0:
            first_frog.health -= damage_to_first

    return 2  # Победа второй жабы


async def run_battles(num_battles):
    results = {1: 0, 2: 0}

    for fight in range(num_battles):
        frog_classes = [BasicFrog, AssassinFrog, AdventurerFrog, CraftsmanFrog]
        frog1 = random.choice(frog_classes)()
        frog2 = random.choice(frog_classes)()

        winner = await battle(frog1, frog2)
        results[winner] += 1

    return results


async def main():
    num_battles = 100
    results = await run_battles(num_battles)
    print(f"Побед первой жабы: {results[1]}")
    print(f"Побед второй жабы: {results[2]}")


if __name__ == "__main__":
    asyncio.run(main())
