from rest_framework import serializers
from .models import Banner

class BannerModelSerializer(serializers.ModelSerializer):
    # 字段声明

    # 模型序列化字段声明
    """轮播图序列化器"""
    class Meta:
        model = Banner
        fields = ["img_url", "link"]
    
    # 验证方法
    
    # 存储数据方法