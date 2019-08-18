# python单元测试
## 依赖包安装
```
pip install pytest
pip install pytest-cov
#not necessary
pip install six --upgrade --ignore-installed six
```

## 被测代码
- dev.py

## 单测代码
- unittest_dev.py

## 单元测试执行命令:

```
py.test *py -r p --junit-xml=result_unittest.xml --cov-report=html --cov-config=.coveragerc --cov=./
```

结果文件：
- result_unittest.xml: xml形式的结果记录
- htmlcov: 单元测试结果报告的目录
