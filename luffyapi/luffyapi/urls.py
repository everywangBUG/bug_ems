"""luffyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 正则路由路径
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

import xadmin
xadmin.autodiscover()

# version模量自动注册需要版本控制的model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 通过xadmin登录
    path(r'xadmin/', xadmin.site.urls),
    # 找到media文件夹下的文件
    re_path(r'media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT }),
    path('', include('home.urls'))
]
