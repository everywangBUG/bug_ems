from django.db import models

class BaseModel(models.Model):
    """基础模型"""
    is_show = models.BooleanField(default=False, verbose_name='是否显示')
    orders = models.IntegerField(default=1, verbose_name='排序')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        # 设置当前的模型在数据迁移的时候不用创建表，即设计为抽象模型
        abstract = True