print("Файл главной ветки проекта после объединения")

import user_input


def main():
  try:
      # Запрашиваем у пользователя два аргумента
      num1 = user_input.get_user_input("Введите первое число: ")
      num2 = user_input.get_user_input("Введите второе число: ")

      # Вычисляем и выводим результаты
      print(f"\nРезультаты вычислений:")
      print(f"{num1} + {num2} = {num1 + num2}")
      print(f"{num1} - {num2} = {num1 - num2}")
      print(f"{num1} * {num2} = {num1 * num2}")
      print(f"{num1} / {num2} = {num1 / num2}")

  except ValueError:
      print("Ошибка: Введите корректное числовое значение.")
main()