import random
import sys

def number_game(lower_limit, upper_limit, attempts):
    secret_number = random.randint(lower_limit, upper_limit)
    
    for _ in range(attempts):
        guess = int(input("Введите число: "))
        
        if guess == secret_number:
            print("Поздравляю, вы угадали число!")
            return True
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")
    
    print("К сожалению, вы не угадали число.")
    return False

if __name__ == "__main__":
    #_, *params = sys.argv
    # Проверяем, что переданы аргументы командной строки
    if len(sys.argv) < 4:
        print("Ошибка! Недостаточно аргументов командной строки.")
        print("Используйте: python имя_файла.py lower_limit upper_limit attempts")
    else:
        # Преобразуем аргументы командной строки в числа
        lower_limit = int(sys.argv[1])
        upper_limit = int(sys.argv[2])
        attempts = int(sys.argv[3])
        
        # Вызываем функцию guess_number с переданными аргументами
        print(number_game(lower_limit, upper_limit, attempts))

