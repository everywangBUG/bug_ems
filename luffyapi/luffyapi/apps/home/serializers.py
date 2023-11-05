from rest_framework import serializers
from .models import Banner, Nav

class BannerModelSerializer(serializers.ModelSerializer):
    # 字段声明

    # 模型序列化字段声明
    """轮播图序列化器"""
    class Meta:
        model = Banner
        fields = ["img_url", "link"]
    
class NavModelSerializer(serializers.ModelSerializer):
    # 字段声明

    # 模型序列化字段声明
    """导航序列化器"""
    class Meta:
        model = Nav
        fields = ["title", "link", 'is_site']