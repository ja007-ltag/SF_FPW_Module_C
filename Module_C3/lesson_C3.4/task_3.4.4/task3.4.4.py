# Создайте любой файл на операционной системе под название input.txt и построчно перепишите его в файл output.txt.

with open("input.txt", "r", encoding="utf8") as f_in:
    with open("output.txt", 'w', encoding="utf8") as f_out:
        for line in f_in:
            f_out.writelines(line)
