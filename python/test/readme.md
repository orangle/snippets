testing
=====

## unittest

怎么写呢？
- 项目单独的目录 tests

怎么运行呢
`python -m unittest tests.test_unit_report -v` 使用模块的方式，可以具体到某个类或者方法

## pytest 

用pytest运行 unittest 

运行一个文件，一个类，一个方法
```
pytest tests/test_unit_report.py -v
pytest tests/test_unit_report.py -v -k "AppcodeInfoTest"
pytest tests/test_unit_report.py -v -k "AppcodeInfoTest and test_get_app_tree_fist"

或者
pytest tests/test_unit_report.py::AppcodeInfoTest -v
pytest tests/test_unit_report.py::AppcodeInfoTest::test_get_appcode_dept1_name -v
```

不显示warnings
```
pytest tests/test_unit_report.py::AppcodeInfoTest::test_get_appcode_dept1_name -v --disable-warnings
```

