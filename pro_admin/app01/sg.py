from sixgod.service import v1
from app01 import models


class SixGodUserInfo(v1.BaseSixGodAdmin):
    pass


v1.site.register(models.UserInfo, SixGodUserInfo)


class SixGodRole(v1.BaseSixGodAdmin):
    pass


v1.site.register(models.Role, SixGodRole)
