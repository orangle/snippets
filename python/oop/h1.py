# coding:utf-8


class A:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        print(self.x)


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y


class C(A):
    def __init__(self, x, y):
        self.x = x
        self.y = y


o = B(1, 2)
print(vars(o))

c = C(1, 2)
print(vars(c))
c.get_x()