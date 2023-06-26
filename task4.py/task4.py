from riddle_game import guess_riddle

riddle = "У меня нет рук, но могу раздавать печеньки. Кто я?"
options = ["Робот", "Кошка", "Волк", "Дракон"]
attempts = 3

result = guess_riddle(riddle, options, attempts)
if result > 0:
    print(f"Загадка отгадана с попытки №{result}.")
else:
    print("Сожалеем, все попытки исчерпаны.")
