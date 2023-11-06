# Generated by Django 2.2.1 on 2023-11-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=500, verbose_name='轮播图标题')),
                ('link', models.CharField(max_length=500, verbose_name='轮播图链接')),
                ('img_url', models.ImageField(blank=True, max_length=255, null=True, upload_to='banner', verbose_name='轮播图地址')),
                ('remark', models.TextField(verbose_name='轮播图备注')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'lufffy_banner',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否显示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('title', models.CharField(max_length=500, verbose_name='导航标题')),
                ('link', models.CharField(max_length=500, verbose_name='导航链接')),
                ('position', models.IntegerField(choices=[(1, '顶部导航'), (2, '底部导航')], default=1, verbose_name='导航位置')),
                ('is_site', models.BooleanField(default=False, verbose_name='是否是站点导航')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
