from django.urls import path
from . import views

urlpatterns = [
    # 路由只识别函数视图，不识别类视图，as_view()作一层转换
    path(r'banner/', views.BannerListAPIView.as_view()),
    path(r'navheader/', views.HeaderNavListAPIView.as_view()),
    path(r'navfooter/', views.FooterNavListAPIView.as_view()),
]
