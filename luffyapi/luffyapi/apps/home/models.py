from django.db import models

# Create your models here.
class Banner(models.Model):
    """轮播图模型"""
    # 模型字段
    title = models.CharField(max_length=500, verbose_name='轮播图标题')
    link = models.CharField(max_length=500, verbose_name='轮播图链接')
    # 图片存在upload下的哪一个子目录中upload_to
    img_url = models.ImageField(upload_to="banner", max_length=255, null=True, blank=True, verbose_name='轮播图地址')
    remark = models.TextField(verbose_name='轮播图备注')
    is_show = models.BooleanField(default=False, verbose_name='是否显示')
    orders = models.IntegerField(default=1, verbose_name='排序')
    is_deleted = models.BooleanField(default=False, verbose_name='是否删除')

    # 表信息声明
    class Meta:
        db_table = 'lufffy_banner'
        verbose_name = '轮播图' 
        verbose_name_plural = verbose_name

    # 自定义方法(自定义显示字段)
    def __str__(self) -> str:
        return self.title