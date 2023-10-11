from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from rekrutacja import settings


class Img(models.Model):
    image = models.ImageField(upload_to='images', blank=True)

    @property
    def get_absolute_image_url(self):
        return "{0}".format(settings.LOCALHOST + self.image.url)

class ImgThumb400(models.Model):
    thumb = models.ImageField(upload_to='thumb400', blank=True)

    @property
    def get_absolute_image_url(self):
        return "{0}".format(settings.LOCALHOST + self.thumb.url)

class ImgThumb200(models.Model):
    thumb = models.ImageField(upload_to='thumb200', blank=True)

    @property
    def get_absolute_image_url(self):
        return "{0}".format(settings.LOCALHOST + self.thumb.url)


class ImgThumb(models.Model):
    thumb = models.ImageField(upload_to='thumb', blank=True)

    @property
    def get_absolute_image_url(self):
        return "{0}".format(settings.LOCALHOST + self.thumb.url)


class TempUrl(models.Model):
    url_hash = models.CharField("Url", blank=False, max_length=32, unique=True)
    expires = models.IntegerField("Expires", validators=[MinValueValidator(300), MaxValueValidator(30000)])