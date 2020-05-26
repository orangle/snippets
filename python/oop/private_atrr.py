class X:
    __table = 'user'

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

print(vars(X))
print(vars(X('user1')))