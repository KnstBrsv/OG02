def get_user_input(prompt, value_type=float):
  """
  Функция запрашивает у пользователя ввод значения с проверкой на корректность.

  Аргументы:
  prompt (str): Сообщение для запроса ввода.
  value_type (type): Ожидаемый тип значения (по умолчанию float).

  Возвращает:
  value_type: Корректное числовое значение указанного типа.
  """
  while True:
      try:
          value = value_type(input(prompt))
          if value <= 0:
              print("Ошибка: введите положительное значение.")
          else:
              return value
      except ValueError:
          print(f"Ошибка: введите корректное значение ({value_type.__name__}).")