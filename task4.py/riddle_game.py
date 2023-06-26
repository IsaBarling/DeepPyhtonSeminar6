import random

def guess_riddle(riddle, options, attempts):
    """
    Функция для угадывания загадки.

    Аргументы:
    - riddle (str): Загадка, которую нужно угадать.
    - options (list): Список с возможными вариантами отгадок.
    - attempts (int): Количество попыток на угадывание.

    Возвращает:
    - int: Номер попытки, с которой была отгадана загадка, или 0, если попытки исчерпаны.
    """
    print("Угадайте загадку!\nУ меня нет рук, но могу раздавать печеньки. Кто я?")
    print(f"У вас {attempts} попыток.")

    # Выбираем случайную отгадку из списка
    correct_answer = random.choice(options)
    
    for attempt in range(1, attempts + 1):
        guess = input(f"Попытка №{attempt}. Ваш ответ: ")
        
        if guess == correct_answer:
            print("Поздравляю, вы угадали загадку!")
            return attempt

    print("Попробуйте еще раз подумать.")
    return 0
