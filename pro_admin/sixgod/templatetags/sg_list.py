from django.template import Library
from types import FunctionType

register = Library()


def table_body(result_list, list_display, sga_obj):
    # for row in result_list:
    #     sub = []
    #     for name in list_display:
    #         val = getattr(row, name)
    #         sub.append(val)
    #     yield sub

    # for row in result_list:
    #     print(row)
    #     yield [getattr(row, name) for name in list_display]

    for row in result_list:
        yield [name(sga_obj, row) if isinstance(name, FunctionType) else getattr(row, name) for name in list_display]


@register.inclusion_tag('sg/md.html')
def func(result_list, list_display, sga_obj):
    tb_obj = table_body(result_list, list_display, sga_obj)
    return {'tb_obj': tb_obj}
