PI = 3.14


def circle_area(r):
    return PI * r ** 2


def rect_area(a, b):
    return a * b


if __name__ == "__main__":
    assert circle_area(5) == 78.5
    assert rect_area(5, 4) == 20
