import random
from riddles import RiddleGame

def guess_riddles(game):
    _riddles_ = {
    "Какой планетой считается самой горячей в Солнечной системе?": ["Венера"],
    "Что это такое: синий, большой, с усами и полностью набит зайцами?": ["Синий кит"],
    "Что можно увидеть с закрытыми глазами?": ["Сон"],
    "Какой город является столицей Италии?": ["Рим"],
    "Какой насекомое может летать задом наперед?": ["Муха"],
    "Как зовут главного героя книги 'Властелин колец' Дж. Р. Р. Толкиена?": ["Фродо"],
    "Самая большая планета в Солнечной системе?": ["Юпитер"],
    "Какая птица считается символом мира?": ["Голубь"],
    "Как называется самая длинная река в мире?": ["Амазонка"],
    "Сколько планет в Солнечной системе?": ["Восемь"]
}

    attempts = 3  # Количество попыток на угадывание
    print(f"У вас {attempts} попыток.")

    for riddle, answers in _riddles_.items():
        print(f"\n{riddle}")
        for i in range(1, attempts + 1):
            answer = input(f"Попытка №{i}. Ваш ответ: ")
            if answer.lower() in map(str.lower, answers):
                print("Поздравляю, вы угадали!")
                game.play_riddle(riddle, i)
                break
            else:
                print("Неверно.")
        else:
            print("Попытки исчерпаны. Правильный ответ: ", random.choice(answers))
            game.play_riddle(riddle, 0)

        continue_game = input("Продолжить игру? (да/нет): ")
        if continue_game.lower() == "нет":
            return

# Запуск игры и угадывание загадок
game = RiddleGame()
guess_riddles(game)

# Вывод результатов угадывания
game.print_results()
