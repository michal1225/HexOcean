from django.contrib import admin

from media.models import Img


@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    pass
