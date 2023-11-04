from django.contrib import admin

# Register your models here.
from rest_framework.generics import ListAPIView
from .models import Banner
from serializers import BannerModelSerializer
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("orders", "-id")
    serializer_class = BannerModelSerializer