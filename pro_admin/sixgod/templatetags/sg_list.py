from django.template import Library

register = Library()


def table_body(result_list, list_display):
    # for row in result_list:
    #     sub = []
    #     for name in list_display:
    #         val = getattr(row, name)
    #         sub.append(val)
    #     yield sub

    for row in result_list:
        yield [getattr(row, name) for name in list_display]


@register.inclusion_tag('sg/md.html')
def func(result_list, list_display):
    tb_obj = table_body(result_list, list_display)
    return {'tb_obj': tb_obj}
