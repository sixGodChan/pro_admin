from django.shortcuts import HttpResponse


class BaseSixGodAdmin(object):
    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site


class SixGodSite(object):
    def __init__(self):
        self._registry = {}
        self.namespace = 'sixgod'
        self.app_name = 'sixgod'

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

            print(app_label, model_name)

            # ret.append(url(r'^%s/%s/' % (app_label, model_name), include(admin_cls_obj.urls)))
            ret.append(url(r'^%s/%s/' % (app_label, model_name), self.login))

        return ret

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace

    def login(self, request):
        return HttpResponse('login')

    def logout(self, request):
        return HttpResponse('logout')


site = SixGodSite()
