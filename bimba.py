import os # Модуль ос для создания папок
import random # Генерация рандом названий (цифр)

while True: # Бесконечный цикл
    try:
        papka = str(random.randint(1, 5432143212)) # генерация названия
        os.mkdir(papka) # Создание папки
    except Exception: # игнор ошибок
        pass
