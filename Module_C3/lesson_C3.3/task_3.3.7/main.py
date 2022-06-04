from function import *


def main():
    r = int(input("Введите радиус круга - r: "))
    a = int(input("Введите сторону прямоугольника - a: "))
    b = int(input("Введите сторону прямоугольника - b: "))

    if circle_area(r) > rect_area(a, b):
        print("Площадь круга больше!")
    else:
        print("Площадь прямоугольника больше!")


if __name__ == "__main__":
    main()
