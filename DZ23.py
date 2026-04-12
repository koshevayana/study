import os

def create_structure():

    os.makedirs("Work/F1")
    os.makedirs("Work/F2/F21")

    with open("Work/w.txt", "w") as f:
        f.write("Это файл w.txt\n")

    with open("Work/F1/f11.txt", "w") as f:
        f.write("f11.txt\n")

    with open("Work/F1/f12.txt", "w") as f:
        f.write("f12.txt\n")

    with open("Work/F1/f13.txt", "w") as f:
        f.write("f13.txt\n")

    with open("Work/F2/F21/f211.txt", "w") as f:
        f.write("f211.txt\n")

    with open("Work/F2/F21/f212.txt", "w") as f:
        f.write("f212.txt\n")

def walk_up(path):

    if not os.path.exists(path):
        return

    items = os.listdir(path)

    for item in items:
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            walk_up(item_path)
        else:
            print(f"Файл: {item_path}")

    if os.path.isdir(path):
        print(f"Папка: {path}")

def walk_top_down(path, indent=""):

    if not os.path.exists(path):
        return

    if os.path.isdir(path):
        print(f"{indent} {os.path.basename(path)}/")
        new_indent = indent + "  "
    else:
        print(f"{indent} {os.path.basename(path)}")
        return

    items = os.listdir(path)
    items.sort()

    for item in items:
        item_path = os.path.join(path, item)
        walk_top_down(item_path, new_indent)


if __name__ == "__main__":
    print("=== Создание структуры папок и файлов ===\n")
    create_structure()
    print("Структура создана!\n")

    print("=== Обход дерева СНИЗУ ВВЕРХ ===\n")
    walk_up("Work")
    print("\n")

    print("=== Обход дерева СВЕРХУ ВНИЗ===\n")
    walk_top_down("Work")
