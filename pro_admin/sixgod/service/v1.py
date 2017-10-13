from django.shortcuts import HttpResponse, render


class BaseSixGodAdmin(object):
    list_display = '__all__'  # 显示全部字段

    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site
        self.request = None

    @property
    def urls(self):
        from django.conf.urls import url
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urlpatterns = [
            url(r'^$', self.changelist_view, name='%s_%s_changelist' % info),
            url(r'^add/$', self.add_view, name='%s_%s_add' % info),
            url(r'^(.+)/delete/$', self.delete_view, name='%s_%s_delete' % info),
            url(r'^(.+)/change/$', self.change_view, name='%s_%s_change' % info),
        ]

        return urlpatterns

    def changelist_view(self, request):
        self.request = request
        result_list = self.model_class.objects.all()

        context = {
            'result_list': result_list,
            'list_display': self.list_display,
            'sga_obj': self,
        }

        return render(self.request, 'sg/changelist_view.html', context)

    def add_view(self, request):
        return HttpResponse('add')

    def delete_view(self, request, pk):
        return HttpResponse('delete')

    def change_view(self, request, pk):
        return HttpResponse('change')


class SixGodSite(object):
    def __init__(self):
        self._registry = {}
        self.namespace = 'sixgod'
        self.app_name = 'sixgod'
        self.request = None

    def register(self, model_class, bsga_class=BaseSixGodAdmin):
        self._registry[model_class] = bsga_class(model_class, self)  # self就是site

    def get_urls(self):
        from django.conf.urls import url, include
        ret = [
            url(r'^login/', self.login, name='login'),
            url(r'^logout/', self.logout, name='logout'),
        ]

        for model_cls, admin_cls_obj in self._registry.items():
            app_label = model_cls._meta.app_label
            model_name = model_cls._meta.model_name

            # print(app_label, model_name)

            ret.append(url(r'^%s/%s/' % (app_label, model_name), include(admin_cls_obj.urls)))

        return ret

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace

    def login(self, request):
        return HttpResponse('login')

    def logout(self, request):
        return HttpResponse('logout')


site = SixGodSite()
