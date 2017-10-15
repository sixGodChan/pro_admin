from sixgod.service import v1
from app01 import models
from django.utils.safestring import mark_safe
from django.urls import reverse


class SixGodUserInfo(v1.BaseSixGodAdmin):
    # table 操作（编辑、删除）
    def option_func(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:
            # 编辑
            reverse_name = '{0}:{1}_{2}_change'.format(self.site.namespace, self.model_class._meta.app_label,
                                                       self.model_class._meta.model_name)
            base_edit_url = reverse(reverse_name, args=(obj.pk,))

            # 携带筛选条件
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelist_filter'] = self.request.GET.urlencode()

            edit_url = '{0}?{1}'.format(base_edit_url, param_dict.urlencode())

            # 删除
            reverse_name = '{0}:{1}_{2}_delete'.format(self.site.namespace, self.model_class._meta.app_label,
                                                       self.model_class._meta.model_name)
            base_edit_url = reverse(reverse_name, args=(obj.pk,))

            # 携带筛选条件
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelist_filter'] = self.request.GET.urlencode()

            del_url = '{0}?{1}'.format(base_edit_url, param_dict.urlencode())

            return mark_safe('<a href="{0}">编辑</a>&nbsp&nbsp<a href="{1}">删除</a>'.format(edit_url, del_url))

    # table checkbox 操作
    def checkbox_func(self, obj=None, is_header=False):
        if is_header:
            # return '<a type="checkbox"></a>'  # 全选
            return '选项'
        else:
            return mark_safe('<input type="checkbox" value="{0}"></a>'.format(obj.pk))

    # table m2m 显示
    def m2m(self, obj=None, is_header=False):
        if is_header:
            return '角色'
        else:
            return [i.name for i in obj.m2m.all()]

    # table 显示字段
    list_display = [checkbox_func, 'id', 'username', 'email', 'ug', m2m, option_func]


v1.site.register(models.UserInfo, SixGodUserInfo)


class SixGodRole(v1.BaseSixGodAdmin):
    # table 操作（编辑、删除）
    def option_func(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:
            # 编辑
            reverse_name = '{0}:{1}_{2}_change'.format(self.site.namespace, self.model_class._meta.app_label,
                                                       self.model_class._meta.model_name)
            base_edit_url = reverse(reverse_name, args=(obj.pk,))

            # 携带筛选条件
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelist_filter'] = self.request.GET.urlencode()

            edit_url = '{0}?{1}'.format(base_edit_url, param_dict.urlencode())

            # 删除
            reverse_name = '{0}:{1}_{2}_delete'.format(self.site.namespace, self.model_class._meta.app_label,
                                                       self.model_class._meta.model_name)
            base_edit_url = reverse(reverse_name, args=(obj.pk,))

            # 携带筛选条件
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelist_filter'] = self.request.GET.urlencode()

            del_url = '{0}?{1}'.format(base_edit_url, param_dict.urlencode())

            return mark_safe('<a href="{0}">编辑</a>&nbsp&nbsp<a href="{1}">删除</a>'.format(edit_url, del_url))

    # table checkbox 操作
    def checkbox_func(self, obj=None, is_header=False):
        if is_header:
            # return '<a type="checkbox"></a>'  # 全选
            return '选项'
        else:
            return mark_safe('<input type="checkbox" value="{0}"></a>'.format(obj.pk))

    list_display = [checkbox_func, 'id', 'name', option_func]


v1.site.register(models.Role, SixGodRole)


class SixGodUserGroup(v1.BaseSixGodAdmin):
    # table 操作（编辑、删除）
    def option_func(self, obj=None, is_header=False):
        if is_header:
            return '操作'
        else:
            # 编辑
            reverse_name = '{0}:{1}_{2}_change'.format(self.site.namespace, self.model_class._meta.app_label,
                                                       self.model_class._meta.model_name)
            base_edit_url = reverse(reverse_name, args=(obj.pk,))

            # 携带筛选条件
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelist_filter'] = self.request.GET.urlencode()

            edit_url = '{0}?{1}'.format(base_edit_url, param_dict.urlencode())

            # 删除
            reverse_name = '{0}:{1}_{2}_delete'.format(self.site.namespace, self.model_class._meta.app_label,
                                                       self.model_class._meta.model_name)
            base_edit_url = reverse(reverse_name, args=(obj.pk,))

            # 携带筛选条件
            from django.http.request import QueryDict
            param_dict = QueryDict(mutable=True)
            if self.request.GET:
                param_dict['_changelist_filter'] = self.request.GET.urlencode()

            del_url = '{0}?{1}'.format(base_edit_url, param_dict.urlencode())

            return mark_safe('<a href="{0}">编辑</a>&nbsp&nbsp<a href="{1}">删除</a>'.format(edit_url, del_url))

    # table checkbox 操作
    def checkbox_func(self, obj=None, is_header=False):
        if is_header:
            # return '<a type="checkbox"></a>'  # 全选
            return '选项'
        else:
            return mark_safe('<input type="checkbox" value="{0}"></a>'.format(obj.pk))

    # table 显示字段
    list_display = [checkbox_func, 'id', 'title', option_func]


v1.site.register(models.UserGroup, SixGodUserGroup)
