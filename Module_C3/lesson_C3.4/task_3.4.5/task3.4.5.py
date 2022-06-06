# Дан файл numbers.txt, компоненты которого являются действительными числами (файл создайте самостоятельно
# и заполните любыми числами, в одной строке одно число).
# Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt.

with open("numbers.txt", "r") as file_num:
    min_num = max_num = float(file_num.readline())

    for line in file_num:
        num = float(line)
        if min_num > num:
            min_num = num
        elif max_num < num:
            max_num = num

res_num = min_num + max_num

with open("output.txt", "w") as file_output:
    file_output.writelines(str(res_num) + "\n")
