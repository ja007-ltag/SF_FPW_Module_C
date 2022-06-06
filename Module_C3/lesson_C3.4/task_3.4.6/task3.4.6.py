# В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную.
# Выведите на экран всех учащихся, чья оценка меньше 3 баллов.

with open("input.txt", 'r', encoding="utf8") as file:
    for line in file:
        point = int(line.strip()[-1])
        if point < 3:
            name = line.strip()[:-2]
            print(name)
