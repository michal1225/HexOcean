from django.contrib import admin

from media.models import Img, ImgThumb400, ImgThumb200, ImgThumb


@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    pass



@admin.register(ImgThumb200)
class ImgThumb200Admin(admin.ModelAdmin):
    pass


@admin.register(ImgThumb400)
class ImgThumb400Admin(admin.ModelAdmin):
    pass


@admin.register(ImgThumb)
class ImgThumbAdmin(admin.ModelAdmin):
    pass