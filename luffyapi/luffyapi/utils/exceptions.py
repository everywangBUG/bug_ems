from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status

import logging

logger = logging.getLogger("django")

# 自定义关于数据库、view中函数的错误信息处理函数
def custom_exception_handler(exc, context):
    """自定义异常处理

    Args:
        exc (_type_): 本次请求发生的异常信息
        context (_type_): 本次请求发生异常的执行上下文(本次请求的request对象，异常发生的时间， 行数等。。。)
    """
    response = exception_handler(exc, context)

    if response is None:
        view = context['view']
        """两种情况，第一种程序没有出错，第二种出错了django或restframework没有识别"""
        if isinstance(exc, DatabaseError):
            # 数据库异常
            logger.error('[%s] %s % (view, exc)')
            response = Response({ "message": "服务器错误, 请联系客服人员!"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response