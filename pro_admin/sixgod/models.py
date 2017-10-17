from django.db import models


class User(models.Model):
    '''
    用户表
    '''
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱')
    role = models.ManyToManyField(to='Role', verbose_name='具有角色', blank=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    '''
    角色
    '''
    caption = models.CharField(verbose_name='角色', max_length=32)
    permissions = models.ManyToManyField(to='Permission', verbose_name='拥有权限', blank=True)

    def __str__(self):
        return self.caption


class Menu(models.Model):
    '''
    菜单
    '''
    caption = models.CharField(verbose_name='菜单名称', max_length=32)
    parent = models.ForeignKey('self', related_name='p', verbose_name='父菜单', null=True, blank=True)

    def __str__(self):
        prev = ""
        parent = self.parent
        while True:
            if parent:
                prev = prev + '-' + str(parent.caption)
                parent = parent.parent
            else:
                break
        return '%s-%s' % (prev, self.caption,)


class Permission(models.Model):
    """
    权限
    /arya/app01/userinfo/add/
    /arya/app01/userinfo/
    /arya/app01/userinfo/1/change
    /arya/app01/userinfo/1/delte
    """
    caption = models.CharField(verbose_name='权限名称', max_length=32)
    # app_label = models.CharField(verbose_name='app名称', max_length=32)
    # app_name = models.CharField(verbose_name='model名称', max_length=32)
    # name = models.CharField(verbose_name='name名称', max_length=32)
    # args = models.CharField(verbose_name='反向创建URL参数(元组格式)', max_length=64, null=True, blank=True)
    # query_params = models.CharField(verbose_name='其他参数', max_length=128, null=True, blank=True)
    # 自动发现
    url = models.CharField(max_length=128)
    menu = models.ForeignKey(Menu, verbose_name='所属菜单', related_name='permissions', null=True, blank=True)

    def __str__(self):
        return "%s" % (self.caption,)
