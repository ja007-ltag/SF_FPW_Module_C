# Выполните реверсирование строк файла (перестановка строк файла в обратном порядке).

with open("input.txt", "r", encoding="utf-8") as file_input:
    with open("output.txt", "w", encoding="utf-8") as file_output:
        for line in reversed(file_input.readlines()):
            file_output.writelines(line)
