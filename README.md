# supermarketDistributionSystem

My college software engineering project.

## 所使用的pip模块

数据库实现

``` bash
pip install pymysql
```

## GUI实现模块

Tkinter Tkinter.ttk Tkinter.messagebox

## 项目结构

``` bash
├─ supermarket
│  ├─ module
│  │  ├─ SupermarketDB.py 数据库封装
│  │  ├─ User.py 用户类定义
│  │  ├─ Order.py 商品类订单类定义
│  │  ├─ ttkcalendar.py 日期选择器
│  │  ├─ __init__.py
│  ├─ tests 测试目录
│  ├─ system.py 系统功能逻辑实现
│  ├─ gui.py GUI实现，项目入口程序
│  ├─ __init__.py
├─ web web端，暂未实现
├─ docs 文档目录
├─ __init__.py
├─ requirements.txt
├─ .gitignore
```

([日期选择器来源](https://svn.python.org/projects/sandbox/trunk/ttk-gsoc/samples/ttkcalendar.py))
