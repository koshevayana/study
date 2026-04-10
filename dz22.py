def peremena(filename, text,  pos1, pos2):
    with open(filename, 'w') as f:
        f.write(text)
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines[pos1-1], lines[pos2-1] = lines[pos2-1],  lines[pos1-1]
    with open(filename, 'w') as f:
        f.writelines(lines)

peremena('peremena.txt',  "замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n", 2, 3)


def reverse_lines(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines.reverse()
    with open(filename, 'w') as f:
        f.writelines(lines)

reverse_lines('reverse.txt', "замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n" )

def file_sum(file1, file2):
    with open(file1, 'r') as f:
        content1 = f.read()
    with open(file2, 'r') as f:
        content2 = f.read()
    new_file='result.txt'
    with open(new_file, 'w') as f:
        f.write(content1 + content2)
    print(f'Создан файл: {new_file}')

file_sum('peremena.txt', 'reverse.txt')

