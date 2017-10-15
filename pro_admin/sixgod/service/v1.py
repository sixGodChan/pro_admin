from django.shortcuts import HttpResponse, render, redirect
from django.urls import reverse


class BaseSixGodAdmin(object):
    list_display = '__all__'  # 显示全部字段
    model_form = None

    def __init__(self, model_class, site):
        self.model_class = model_class
        self.site = site
        self.request = None

        self.app_label = self.model_class._meta.app_label
        self.model_name = self.model_class._meta.model_name

    @property
    def urls(self):
        from django.conf.urls import url
        info = self.app_label, self.model_name
        urlpatterns = [
            url(r'^$', self.changelist_view, name='%s_%s_changelist' % info),
            url(r'^add/$', self.add_view, name='%s_%s_add' % info),
            url(r'^(.+)/delete/$', self.delete_view, name='%s_%s_delete' % info),
            url(r'^(.+)/change/$', self.change_view, name='%s_%s_change' % info),
        ]

        return urlpatterns

    def get_ModelForm(self):
        if self.model_form:
            return self.model_form
        else:
            from django.forms import ModelForm
            class MyModelForm(ModelForm):
                class Meta:
                    model = self.model_class
                    fields = '__all__'

            # type 创建类
            # _m = type('Meta', (object,), {'model': self.model_class, 'fields': '__all__'})
            # MyModelForm = type('MyModelForm', (ModelForm), {'Meta': _m})

            return MyModelForm

    def changelist_view(self, request):
        # 列表页：添加按钮
        from django.http.request import QueryDict
        param_dict = QueryDict(mutable=True)
        if request.GET:
            param_dict['_changelist_filter'] = request.GET.urlencode()

        base_add_url = reverse('{0}:{1}_{2}_add'.format(self.site.namespace, self.app_label, self.model_name))
        add_url = '{0}?{1}'.format(base_add_url, param_dict.urlencode())

        # 列表页：表格
        self.request = request
        result_list = self.model_class.objects.all()

        context = {
            'result_list': result_list,
            'list_display': self.list_display,
            'sga_obj': self,
            'add_url': add_url,
        }

        return render(self.request, 'sg/changelist_view.html', context)

    def add_view(self, request):
        if request.method == 'GET':
            form = self.get_ModelForm()()
            context = {
                'form': form,
                'sga_obj': self,
            }
            return render(request, 'sg/add_view.html', context)
        else:
            form = self.get_ModelForm()(data=request.POST, files=request.FILES)
            if form.is_valid():
                obj = form.save()
                # 如果是popup方式过来
                if request.GET.get('popup_id'):
                    popup_tag_id = request.GET.get('popup_id')
                    context = {'popup_tag_id': popup_tag_id, 'option_id': obj.pk, 'option_text': str(obj)}
                    return render(request, 'sg/popup_response.html', context)
                # popup方式结束
                base_add_url = reverse(
                    '{0}:{1}_{2}_changelist'.format(self.site.namespace, self.app_label, self.model_name))
                add_url = '{0}?{1}'.format(base_add_url, request.GET.get('_changelist_filter'))

                return redirect(add_url)

        context = {
            'form': form
        }
        return render(request, 'sg/add_view.html', context)

    def delete_view(self, request, pk):
        if request.method == 'GET':
            if pk:
                obj = self.model_class.objects.filter(pk=pk).delete()
                if obj:
                    base_add_url = reverse(
                        '{0}:{1}_{2}_changelist'.format(self.site.namespace, self.app_label, self.model_name))
                    edit_url = '{0}?{1}'.format(base_add_url, request.GET.get('_changelist_filter'))

                    return redirect(edit_url)

    def change_view(self, request, pk):
        obj = self.model_class.objects.filter(pk=pk).first()
        if request.method == 'GET':
            form = self.get_ModelForm()(instance=obj)
            context = {
                'form': form
            }
            return render(request, 'sg/change_view.html', context)
        else:
            form = self.get_ModelForm()(instance=obj, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                base_add_url = reverse(
                    '{0}:{1}_{2}_changelist'.format(self.site.namespace, self.app_label, self.model_name))
                edit_url = '{0}?{1}'.format(base_add_url, request.GET.get('_changelist_filter'))

                return redirect(edit_url)
        context = {
            'form': form
        }
        return render(request, 'sg/change_view.html', context)

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

