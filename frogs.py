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

    @abstractmethod
    def get_initiative(self):
        """Возвращает значение инициативы."""
        pass

    def get_damage(self):
        """Возвращает случайное значение урона в диапазоне [attack / 2; attack]."""
        return random.randint(self.attack // 2, self.attack)

    def get_armor(self):
        """Возвращает случайное значение брони в диапазоне [0; armor]."""
        return random.randint(0, self.armor)


class BasicFrog(Frog):

    def get_initiative(self):
        return random.randint(1, 20)


class AssassinFrog(Frog):

    def __init__(self):
        super().__init__(health_multiplier=1.25)

    def get_initiative(self):
        return random.randint(1, 20) + 5


class AdventurerFrog(Frog):

    def get_initiative(self):
        return random.randint(1, 20) + 3

    def get_damage(self):
        """Возвращает случайное значение урона в диапазоне [attack / 2; attack]."""
        return random.randint(self.attack // 2, self.attack) * 1.5


class CraftsmanFrog(Frog):

    def __init__(self):
        super().__init__(armor_multiplier=2.0)

    def get_initiative(self):
        return random.randint(1, 20) - 2

