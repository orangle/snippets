# coding:utf-8
"""
变量注入到函数local作用域里面，字符变量名字之间的运算
"""
exp1 = "a + b * c"


class Dict2Obj(object):
    """
    Turns a dictionary into a class
    """
    def __init__(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])
    def __repr__(self):
        """"""
        return "<Dict2Obj: %s>" % self.__dict__

def test_eval(a, b, c):
    return eval(exp1)

print("r1", test_eval(1, 3, 0))


# 替换变量
def test_replace(a, exp):
    for k, v in a.items():
        if k in exp:
            exp = exp.replace(k, str(v))
    return eval(exp)

r2 = test_replace({"a":1, "b":3, "c": 0}, exp1)
print("r2", r2) 

def test_local(a, exp):
    exec('b = a["b"]')
    print(b)

r22 = test_local({"a":1, "b":3, "c": 0}, exp1)
print("r22", r22) 

# 一个库, 要学会原理
from py_expression_eval import Parser
parser = Parser()

print("r3", parser.parse(exp1).evaluate({"a":1, "b":3, "c": 0}))
# print("r3", parser.parse("(a+b)/c").evaluate({"a":1, "b":3, "c": 0}))


# sympy
