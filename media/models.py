import os
import pathlib
import urllib as urllib
from urllib import request

from django.core.files import File
from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail

from rekrutacja.settings import MEDIA_ROOT


class Img(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    id = models.AutoField(primary_key=True, null=False)

    def cache(self):
        if self.id and not self.image:
            result = request.urlretrieve(str(self.id))
            self.image.save(
                os.path.basename(str(self.id)),
                File(open(result[0], 'rb'))
            )
            self.save()
