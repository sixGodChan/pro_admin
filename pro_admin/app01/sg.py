from sixgod.service import v1
from app01 import models
from django.utils.safestring import mark_safe
from django.urls import reverse


class SixGodUserInfo(v1.BaseSixGodAdmin):
    # table 操作（编辑）
    def edit_func(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:
            reverse_name = '{0}:{1}_{2}_change'.format(self.site.namespace, self.model_class._meta.app_label,
                                                       self.model_class._meta.model_name)
            url = reverse(reverse_name, args=(obj.pk,))
            return mark_safe('<a href="{0}">编辑</a>'.format(url))

    # table checkbox 操作
    def checkbox_func(self, obj=None, is_header=False):
        if is_header:
            # return '<a type="checkbox"></a>'  # 全选
            return '选项'
        else:
            return mark_safe('<input type="checkbox" value="{0}"></a>'.format(obj.pk))

    # table 显示字段
    list_display = [checkbox_func, 'id', 'username', 'email', edit_func]


v1.site.register(models.UserInfo, SixGodUserInfo)


class SixGodRole(v1.BaseSixGodAdmin):
    list_display = ['id', 'name']


v1.site.register(models.Role, SixGodRole)
