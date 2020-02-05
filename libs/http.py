from django.conf import settings
from django.http import JsonResponse

from libs import errors


def render_json(code=errors.OK, data=None):
    """
    json 返回格式
    {
        "code": 0,
        "data": {
        },
    }

    :param code: 错误码
    :param data: 接口数据
    :return:
    """
    result = {
        'code': code
    }

    if data:
        result['data'] = data

    if settings.DEBUG:
        json_dumps_params = {
            'ensure_ascii': False,
            'indent': 4
        }
    else:
        json_dumps_params = {
            'separators': (',', ':')
        }

    return JsonResponse(data=result, json_dumps_params=json_dumps_params)