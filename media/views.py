from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView
from media.models import Img
from media.utils import CheckGroupPermissions, ConvertImage
from media.serializers import ImgSerializer


class ListImagesThumbnails(APIView):
    def post(self, request):
        serializer = ImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        image_converter = ConvertImage()
        qs = Img.objects.last()
        width = None
        height = None
        if CheckGroupPermissions.is_in_group(user=self.request.user, group_name='Premium'):
            if qs is None:
                return Response("No images in database!")
            return Response({
                "Thumbnail 200px height:": image_converter.convertTo200Height(qs=qs),
                "Thumbnail 400px height:": image_converter.convertTo400Height(qs=qs),
                "Original image:": qs.get_absolute_image_url
            })
        elif CheckGroupPermissions.is_in_group(user=self.request.user, group_name='Basic'):
            if qs is None:
                return Response("No images in database!")
            return Response({
                "Thumbnail 200px height:": image_converter.convertTo200Height(qs=qs),
            })
        elif CheckGroupPermissions.is_in_group(user=self.request.user, group_name='Enterprise'):
            if qs is None:
                return Response("No images in database!")
            return Response({
                "Thumbnail 200px height:": image_converter.convertTo200Height(qs=qs),
                "Thumbnail 400px height:": image_converter.convertTo400Height(qs=qs),
                "Original image:": qs.get_absolute_image_url
            })
        elif CheckGroupPermissions.is_in_group(user=self.request.user, group_name='admin'):
            if qs is None:
                return Response("No images in database!")
            # self.request.data.update({"width": 100, "height": 100})
            width = int(self.request.data.get('width'))
            height = int(self.request.data.get('height'))

            if width is None or height is None:
                return Response("You need to pass width and height in request!")
            else:
                return Response({
                "Thumbnail 200px height:": image_converter.convertTo200Height(qs=qs),
                "Thumbnail 400px height:": image_converter.convertTo400Height(qs=qs),
                "Thumbnail:": image_converter.convert(qs=qs, request=self.request),
                "Original image:": qs.get_absolute_image_url
            })
        else:
            return Response("Permissions denied")
