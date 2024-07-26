Игра "Битва жаб" создана с использованием принципов ООП, асинхронного программирования и библиотеки random на Python.

Так же я добавила логику инициативы и функции для проверки баланса игры в файле balance_checker.py

# Технологии
Асинхронное программирование: для проведения боев между жабами с использованием асинхронных циклов.

ООП: для определения классов жаб и их характеристик.

Библиотека random: для генерации случайных значений, таких как инициатива и урон.


# Структура проекта
frogs.py - содержит определение базового класса Frog и классов-наследников BasicFrog, AssassinFrog, AdventurerFrog и CraftsmanFrog.

game.py - реализует логику боя между двумя жабами и запускает асинхронные циклы для проведения 100 боев.

balance_checker.py - реализует функцию для проверки баланса различных классов жаб, проводя серию боев между ними.

# Запуск проекта

Требования

- Python 3.7 или более поздняя версия

1) Клонируйте репозиторий на свой компьютер

2) Перейдите в директорию проекта

3) Запустите game.py

Программа запустит два асинхронных цикла, каждый из которых проведет 100 боев между двумя жабами. Результаты боев будут выведены в консоль.
Или вы можете запустить balance_checker.py для того, чтобы посмотреть, насколько сбалансированы классы жаб
