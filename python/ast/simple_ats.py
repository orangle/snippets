# coding:utf-8
import inspect, ast

# source = inspect.getsource(func)
# tree = ast.parse(source)

# pip install 
from meta.decompiler import decompile_func
tree = decompile_func(lambda x: x + 1)


