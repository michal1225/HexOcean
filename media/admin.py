from django.contrib import admin

from media.models import ImgBasic, ImgPremium, ImgEnterprise


@admin.register(ImgBasic)
class ImgBasicAdmin(admin.ModelAdmin):
    pass


@admin.register(ImgPremium)
class ImgPremiumAdmin(admin.ModelAdmin):
    pass


@admin.register(ImgEnterprise)
class ImgEnterpriseAdmin(admin.ModelAdmin):
    pass
