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
        yield [name(sga_obj, obj=row) if isinstance(name, FunctionType) else getattr(row, name) for name in list_display]


def table_head(list_display, sga_obj):
    # for name in list_display:
    #     if isinstance(name, FunctionType):
    #         yield name(sga_obj, is_header=True)
    #     else:
    #         yield sga_obj.model_class._meta.get_field(name).verbose_name

    for name in list_display:
        yield name(sga_obj, is_header=True) if isinstance(name, FunctionType) else sga_obj.model_class._meta.get_field(name).verbose_name


@register.inclusion_tag('sg/md.html')
def func(result_list, list_display, sga_obj):
    tb_obj = table_body(result_list, list_display, sga_obj)
    th_obj = table_head(list_display, sga_obj)
    return {'th_obj': th_obj, 'tb_obj': tb_obj}
