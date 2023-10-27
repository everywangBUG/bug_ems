## 创建虚拟环境
### 虚拟环境包安装
1. `pip install virtualenv`
2. 创建虚拟环境，会创建一个环境名称的文件夹，放置所有的环境
3. `virtualenv 环境名称 --python=python3.9.13`，这是已经加入全局的环境的做法
4. `virtualenv 环境名称 --python='E:\python\python3.9.13.exe`，这是没有加入全局环境的做法

### 激活和退出虚拟环境
1. `cd Scripts` 进入虚拟环境Scripts目录
2. `source activate` 激活虚拟环境
3. `deactivate` 退出虚拟环境
4. 在激活的虚拟环境中安装包，会安装到虚拟环境中
5. `pip install drango==2.1`安装django2.1，注意避免安装版本和python版本高低不匹配的问题

### 搭建项目环境(django + 虚拟环境)
1. 搭建django环境 `django-admin startproject bug_ems`
2. 创建app01 `python manage.py startapp app01`

## 本地配置local_settings.py
1. 创建一个local_settings.py文件，并加入以下代码，local_settings.py不能泄露
```python
try:
    from .local_settings import *
except ImportError:
    pass
```


