class X:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value 

x = X('lzz')
print(x.name)
x.name = 'abc'
print(x.name)