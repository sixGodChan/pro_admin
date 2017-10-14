from django.template import Library
from types import FunctionType

register = Library()


def table_body(result_list, list_display, sga_obj):
    # for row in result_list:
    #     if list_display == '__all__':
    #         yield [str(row)]
    #     else:
    #         sub = []
    #         for name in list_display:
    #             if isinstance(name, FunctionType):
    #                 val = name(sga_obj, obj=row)
    #             else:
    #                 val = getattr(row, name)
    #             sub.append(val)
    #         yield sub

    for row in result_list:
        if list_display == '__all__':
            yield [str(row)]
        else:
            yield [name(sga_obj, obj=row) if isinstance(name, FunctionType) else getattr(row, name) for name in
                   list_display]


def table_head(list_display, sga_obj):
    if list_display == '__all__':
        yield '对象列表'
    else:
        # for name in list_display:
        #     if isinstance(name, FunctionType):
        #         yield name(sga_obj, is_header=True)
        #     else:
        #         yield sga_obj.model_class._meta.get_field(name).verbose_name

        for name in list_display:
            # sga_obj.model_class._meta.get_field(name) 获取model类对象的属性
            yield name(sga_obj, is_header=True) if isinstance(name,
                                                              FunctionType) else sga_obj.model_class._meta.get_field(
                name).verbose_name


@register.inclusion_tag('sg/md.html')
def func(result_list, list_display, sga_obj):
    tb_obj = table_body(result_list, list_display, sga_obj)
    th_obj = table_head(list_display, sga_obj)
    return {'th_obj': th_obj, 'tb_obj': tb_obj}
