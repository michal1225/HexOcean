from django.db import models
from rekrutacja import settings


class ImgBasic(models.Model):
    image = models.ImageField(upload_to='images', blank=True)

    @property
    def get_absolute_image_url(self):
        return "{0}".format(settings.LOCALHOST + self.image.url)

class ImgPremium(models.Model):
    image = models.ImageField(upload_to='images', blank=True)

    @property
    def get_absolute_image_url(self):
        return "{0}".format(settings.LOCALHOST + self.image.url)

class ImgEnterprise(models.Model):
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