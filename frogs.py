import random
from abc import ABC, abstractmethod


class Frog(ABC):
    BASE_ATTACK = 15
    BASE_HEALTH = 150
    BASE_ARMOR = 5

    def __init__(self, attack_multiplier=1.0, health_multiplier=1.0, armor_multiplier=1.0):
        self.attack = int(self.BASE_ATTACK * attack_multiplier)  # Базовая атака
        self.health = int(self.BASE_HEALTH * health_multiplier)  # Базовое здоровье
        self.armor = int(self.BASE_ARMOR * armor_multiplier)  # Базовая броня

    def get_initiative(self):
        """Возвращает значение инициативы."""
        return random.randint(1, 20)

    def get_damage(self):
        """Возвращает случайное значение урона в диапазоне [attack / 2; attack]."""
        return random.randint(self.attack // 2, self.attack)

    def get_armor(self):
        """Возвращает случайное значение брони в диапазоне [0; armor]."""
        return random.randint(0, self.armor)

    @abstractmethod
    def description(self):
        pass


class BasicFrog(Frog):

    def description(self):
        return (
            "Basic Frog: A well-rounded frog with balanced abilities. "
            "It has average attack, health, and armor values, making it a versatile choice."
        )


class AssassinFrog(Frog):

    def __init__(self):
        super().__init__(health_multiplier=1.25)

    def description(self):
        return (
            "Assassin Frog: A stealthy frog with high health. "
            "It excels in surviving longer in battles, allowing it to outlast opponents."
        )


class AdventurerFrog(Frog):

    def get_damage(self):
        """Возвращает случайное значение урона в диапазоне [attack / 2; attack]."""
        return random.randint(self.attack // 2, self.attack) * 1.5

    def description(self):
        return (
            "Adventurer Frog: A daring frog with high attack power. "
            "It deals increased damage, making it a formidable opponent in combat."
        )


class CraftsmanFrog(Frog):

    def __init__(self):
        super().__init__(armor_multiplier=2.0)

    def description(self):
        return (
            "Craftsman Frog: A sturdy frog with high armor and health. "
            "It is designed to withstand attacks, making it a tank in battles."
        )

