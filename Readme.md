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

## vscode选择pyton解释器
* `ctrl+shift+p`打开命令面板
* `Python: Select Interpreter`选择解释器，输入虚拟环境目录


## 项目目录结构
```
luffy/
  ├── docs/          # 项目相关资料保存目录
  ├── luffycity/     # 前端项目目录
  ├── luffyapi/      # 后端项目目录
       ├── logs/          # 项目运行时/开发时日志目录
       ├── manage.py
       ├── luffyapi/      # 项目主应用，开发时的代码保存
       │    ├── apps/      # 开发者的代码保存目录，以模块[子应用]为目录保存
       │    ├── libs/      # 第三方类库的保存目录[第三方组件、模块]
       │    ├── settings/
       │         ├── dev.py   # 项目开发时的本地配置
       │         ├── prod.py  # 项目上线时的运行配置
       │    ├── urls.py    # 总路由
       │    ├── utils/     # 多个模块[子应用]的公共函数类库[自己开发的组件]
       └── scripts/       # 保存项目运营时的脚本文件
```
1. 重置目录结构后运行项目报错 `The SECRET_KEY setting must not be empty.`
2. 在settings目录下的__init__.py中加入 `SECRET_KEY = "41ccd_4530%#￥fkg43432" DEBUG = True`

## 日志和异常处理
### 日志配置
1. 在dev.py文件中配置日志文件

### 异常处理模块

## 数据库创建和连接
1. 创建数据库 `create database luffy character set utf8mb4;`
2. 为当前的项目创建数据库用户，这个用户只能看到这个数据库，identified设置密码 `create user luffy_user identified by 'luffy';`
3. 赋予所有的权限在任意主机下面('%')给luffy_user `grant all on luffy.* to 'luffy_user'@'%';`
4. 刷新权限 `flush privileges;`
5. `exit` 退出数据库，再重新连接数据库，输入用户名和密码 `mysql -uluffy_user -pluffy;`
6. 项目主模块下__init__.py文件中配置数据库连接信息 `pymysql.install_as_MySQLdb()`

### windows更改host
1. 进入到`C:\Windows\System32\drivers\etc`
2. 修改hosts文件

### 解决跨域
1. 安装`pip install django-cors-headers`
2. 在dev文件中INSTALLED_APPS下面加入 `'corsheaders',`
3. 配置settings.py文件，在`MIDDLEWARE`中添加`'corsheaders.middleware.CorsMiddleware'`
4. 配置`CORS_ORIGIN_ALLOW_ALL = True`