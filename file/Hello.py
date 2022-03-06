
class Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("我的名字叫：", self.name, "我今年：", self.age)

    def cheng(self, a, b):
        print(a * b)


class Son(Father):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def jia(self, a, b):
        print(a + b)

class Test:
    def __init__(self):
        self.a = "123456"
        self.b = "456789"
        self.c = 123

    def jia(self, a, *b):
        sum = a
        for i in b:
            sum = sum + i
        return sum + self.c



if __name__ == "__main__":
        son = Son("peter", 20, 180)
        son.cheng(85, 102)
        print(son.name)