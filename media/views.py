import sys
from io import BytesIO

import np as np
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from rest_framework import viewsets

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from rest_framework.views import APIView
from media.models import ImgBasic, ImgThumb400, ImgThumb200, ImgPremium, ImgEnterprise
from media.serializers import ImgEnterpriseSerializer, ImgPremiumSerializer, ImgBasicSerializer
from rekrutacja import settings


class ImgBasicViewSet(viewsets.ModelViewSet):
    queryset = ImgBasic.objects.order_by('id')
    serializer_class = ImgBasicSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ImgPremiumViewSet(viewsets.ModelViewSet):
    queryset = ImgPremium.objects.order_by('id')
    serializer_class = ImgPremiumSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ImgEnterpriseViewSet(viewsets.ModelViewSet):
    queryset = ImgEnterprise.objects.order_by('id')
    serializer_class = ImgEnterpriseSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ListImagesThumbnails(APIView):
    def get(self, request):
        global thumb400_url, thumb200_url
        qs = ImgPremium.objects.last()
        output_400 = (400, 400)
        output_200 = (200, 200)
        img_name = qs.image.name.split('.')[0]
        img = Image.open(qs.image)

        if img.height > 400:
            img.thumbnail(output_400)
            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG', quality=60)
            thumbnails = InMemoryUploadedFile(thumb_io, 'ImageField', f"{img_name}_thumb.jpg",
                                                   'image/jpeg', sys.getsizeof(output_400), None)
            thumb_object = ImgThumb400.objects.create()
            thumb_object.thumb.save(thumbnails.name, thumbnails)
            thumb400_url = thumb_object.get_absolute_image_url

        if img.height > 200:
            img.thumbnail(output_200)
            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG', quality=60)
            thumbnails = InMemoryUploadedFile(thumb_io, 'ImageField', f"{img_name}_thumb.jpg",
                                              'image/jpeg', sys.getsizeof(output_400), None)
            thumb_object = ImgThumb200.objects.create()
            thumb_object.thumb.save(thumbnails.name, thumbnails)
            thumb200_url = thumb_object.get_absolute_image_url
        return Response({
            "Thumbnail 400px height:": thumb400_url,
            "Thumbnail 200px height:": thumb200_url,
        })





