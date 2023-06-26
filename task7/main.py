from date_validator import is_valid_date

date = input("Введите дату в формате DD.MM.YYYY: ")

if is_valid_date(date):
    print("Дата существует.")
else:
    print("Дата не существует.")
