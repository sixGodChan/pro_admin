class BaseSixGodAdmin(object):
    def __int__(self, model_class, site):
        self.model_class = model_class
        self.site = site


class SixGodSite(object):
    def __init__(self):
        self._registry = {}
        self.namespace = 'sixgod'
        self.app_name = 'sixgod'

    def register(self, model_class, admin_class=BaseSixGodAdmin):
        self._registry[model_class] = admin_class(model_class, self)  # self就是site


site = SixGodSite()
