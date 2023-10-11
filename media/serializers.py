from rest_framework import serializers

from media.models import Img


class ImgSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(required=True)

    def create(self, validated_data):
        img = Img.objects.create(image=validated_data.get('image'))
        return img

    class Meta:
        model = Img
        fields = ['image', 'id']
