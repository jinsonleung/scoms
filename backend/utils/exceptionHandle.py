from rest_framework.views import exception_handler
from django.http import JsonResponse
import logging


def base_exception_handler(exc, context):
    """
    用于处理DRF的异常定制返回，目的是统一返回信息，只有DRF出现异常时才会执行，其他情况不执行
    exc: 是个对象，本次发生的异常对象
    context：是个字典，本次发生异常时的上下文环境信息
            所谓的上下文就是python解释器在执行代码时保存在内存当中的变量、函数、类、对象、模块等一系列信息组件的环境信息
    """
    # 1.先让DRF把自己能处理的异常，先处理完成
    logging.debug('DRF主动提示异常')
    response = exception_handler(exc, context)
    # 2.如果response返回在是None，则当前异常DRF无法处理，就需要自定义处理异常的逻辑代码
    if not response:
        pass
        # print('+' * 128)
        # print(exc)
        # print('+' * 128)
        # response = JsonResponse({"message": str(exc), "errorCode": 1, "data": {}})
    else:
        logging.debug(response.data)
        msg = ''
        for key in response.data:
            if key in ('detail', 'non_field_errors'):
                msg += '%s' % (';'.join(response.data[key])) if isinstance(response.data[key], list) else (response.data[key])
            else:
                msg += '%s：%s ' % (key, ';'.join(response.data[key]))
        code = 0 if response.status_code == 200 else 2
        return JsonResponse({"error_msg": msg, "error_code": code, "error_data": {}}, status=response.status_code, json_dumps_params={'ensure_ascii': False})
    return response

