import os
import datetime

user_path = input("Введите путь для проверки: ")

if os.path.exists(user_path):
    abs_path = os.path.abspath(user_path)

    if os.path.isfile(user_path):
        path_type = "Файл"
    elif os.path.isdir(user_path):
        path_type = "Директория"
    else:
        path_type = "Другой тип"

    file_size = None
    last_change_formatted = None

    if path_type == "Файл":
        file_size_bytes = os.path.getsize(user_path)

        if file_size_bytes < 1024:
            file_size = f"{file_size_bytes} Б"
        elif file_size_bytes < 1024 * 1024:
            file_size = f"{file_size_bytes / 1024} КБ"
        elif file_size_bytes < 1024 * 1024 * 1024:
            file_size = f"{file_size_bytes / (1024 * 1024)} МБ"
        else:
            file_size = f"{file_size_bytes / (1024 * 1024 * 1024)} ГБ"

        last_change = os.path.getmtime(user_path)
        last_change_formatted = datetime.datetime.fromtimestamp(last_change).strftime('%d.%m.%Y %H:%M:%S')

    print("\n" + "=" * 40)
    print("ИНФОРМАЦИЯ О ПУТИ")
    print("=" * 40)
    print(f"Путь: {user_path}")
    print(f"Абсолютный путь: {abs_path}")
    print(f"Тип: {path_type}")

    if path_type == "Файл":
        print(f"Размер: {file_size}")
        print(f"Последнее изменение: {last_change_formatted}")

    print("=" * 40)
else:
    print("Указанный путь не существует.")