对比测试
======
测试文件大小 30916563， 30M，格式类nginx access log


python re, re没有 compile 
```
▶ python regex_vs_split.py
total bytes: 96130099518 cost: 5.805 qps: 92174.132
```

python re, re compile之后
```
▶ python regex_vs_split.py
total bytes: 96130099518 cost: 5.324 qps: 100500.519
```

python split 之后分析
```
▶ python regex_vs_split.py
total bytes: 96130191409 cost: 3.957 qps: 135215.152
```
