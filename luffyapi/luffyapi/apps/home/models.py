from django.db import models

class BaseModel(models.Model):
    """基础模型"""
    is_show = models.BooleanField(default=False, verbose_name='是否显示')
    orders = models.IntegerField(default=1, verbose_name='排序')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

# Create your models here.
class Banner(BaseModel, models.Model):
    """轮播图模型"""
    # 模型字段
    title = models.CharField(max_length=500, verbose_name='轮播图标题')
    link = models.CharField(max_length=500, verbose_name='轮播图链接')
    # 图片存在upload下的哪一个子目录中upload_to
    img_url = models.ImageField(upload_to="banner", max_length=255, null=True, blank=True, verbose_name='轮播图地址')
    remark = models.TextField(verbose_name='轮播图备注')

    # 表信息声明
    class Meta:
        db_table = 'lufffy_banner'
        verbose_name = '轮播图' 
        verbose_name_plural = verbose_name

    # 自定义方法(自定义显示字段)
    def __str__(self) -> str:
        return self.title

class Nav(BaseModel, models.Model):
    """导航模型"""
    # 模型字段
    POSITION_CHOICES = (
        (1, '顶部导航'),
        (2, '底部导航'),
    )
    title = models.CharField(max_length=500, verbose_name='导航标题')
    link = models.CharField(max_length=500, verbose_name='导航链接')
    position = models.IntegerField(choices=POSITION_CHOICES, default=1, verbose_name='导航位置')
    is_site = models.BooleanField(default=False, verbose_name='是否是站点导航')

    class Meat:
        db_table = 'lufffy_nav'
        verbose_name = '导航'
        verbose_name_plural = verbose_name

        def __str__(self) -> str:
            return self.title