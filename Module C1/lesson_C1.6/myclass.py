class MyClass:
    def fun(self):
        return 155 + 2 - 2


mc2 = MyClass()
print("it's for test 2", mc2.fun())
print(__name__)

if __name__ == "__main__":
    mc = MyClass()
    print("It's 1 for test", mc.fun())
