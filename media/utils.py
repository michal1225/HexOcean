import sys
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.response import Response

from media.models import ImgThumb200, ImgThumb400, ImgThumb


class CheckGroupPermissions:
    def is_in_group(user, group_name):
        try:
            return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
        except Group.DoesNotExist:
            return False


class ConvertImage:
    def convertTo200Height(self, qs):
        global thumb200_url
        thumb_object = None
        img_name = qs.image.name.split('.')[0]
        img = Image.open(qs.image)
        output_200 = (200, 200)
        img.thumbnail(output_200)
        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG', quality=60)
        thumbnails = InMemoryUploadedFile(thumb_io, 'ImageField', f"{img_name}_thumb.jpg",
                                          'image/jpeg', sys.getsizeof(output_200), None)
        for image in ImgThumb200.objects.all():
            if image.thumb.name == 'thumb200/' + img_name[7:] + '_thumb.jpg':
                thumb_object = image
        if thumb_object is not None:
            thumb200_url = thumb_object.get_absolute_image_url
        else:
            thumb_object = ImgThumb200.objects.create()
            thumb_object.thumb.save(thumbnails.name, thumbnails)
            thumb200_url = thumb_object.get_absolute_image_url

        return thumb200_url

    def convertTo400Height(self, qs):
        global thumb400_url
        thumb_object = None
        img_name = qs.image.name.split('.')[0]
        img = Image.open(qs.image)
        output_400 = (400, 400)
        img.thumbnail(output_400)
        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG', quality=60)
        thumbnails = InMemoryUploadedFile(thumb_io, 'ImageField', f"{img_name}_thumb.jpg",
                                          'image/jpeg', sys.getsizeof(output_400), None)
        for image in ImgThumb400.objects.all():
            if image.thumb.name == 'thumb400/' + img_name[7:] + '_thumb.jpg':
                thumb_object = image
        if thumb_object is not None:
            thumb400_url = thumb_object.get_absolute_image_url
        else:
            thumb_object = ImgThumb400.objects.create()
            thumb_object.thumb.save(thumbnails.name, thumbnails)
            thumb400_url = thumb_object.get_absolute_image_url
        return thumb400_url

    def convert(self, qs, request):
        global thumb_url
        thumb_object = None
        img_name = qs.image.name.split('.')[0]
        img = Image.open(qs.image)
        try:
            output = (int(request.data.get('width')), int(request.data.get('height')))
        except:
            return Response("You must send int width and height in request")
        img.thumbnail(output)
        thumb_io = BytesIO()
        img.save(thumb_io, format='JPEG', quality=60)
        thumbnails = InMemoryUploadedFile(thumb_io, 'ImageField', f"{img_name}_thumb.jpg",
                                          'image/jpeg', sys.getsizeof(output), None)
        for image in ImgThumb.objects.all():
            if image.thumb.name == 'thumb/' + img_name[7:] + '_thumb.jpg':
                thumb_object = image
        if thumb_object is not None:
            thumb_url = thumb_object.get_absolute_image_url
        else:
            thumb_object = ImgThumb.objects.create()
            thumb_object.thumb.save(thumbnails.name, thumbnails)
            thumb_url = thumb_object.get_absolute_image_url
        return thumb_url
