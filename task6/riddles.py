class RiddleGame:
    def __init__(self):
        self._results = {}

    def play_riddle(self, riddle, attempt):
        if riddle in self._results:
            self._results[riddle].append(attempt)
        else:
            self._results[riddle] = [attempt]

    def print_results(self):
        print("Результаты угадывания:")
        for riddle, attempts in self._results.items():
            result_str = ", ".join(str(a) for a in attempts)
            print(f"Загадка: {riddle}. Попытки: {result_str}")
