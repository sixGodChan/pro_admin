from django.apps import AppConfig


class SixgodConfig(AppConfig):
    name = 'sixgod'

    # 项目启动执行每个app的sg.py
    def ready(self):
        super(SixgodConfig, self).ready()

        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('sg')
