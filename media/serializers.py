from rest_framework import serializers

from media.models import ImgBasic, ImgEnterprise, ImgPremium


class ImgBasicSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(required=True)
    def create(self, validated_data):
        img = ImgBasic.objects.create(image=validated_data.get('image'))
        return img
    class Meta:
        model = ImgBasic
        fields = ['image', 'id']

class ImgPremiumSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(required=True)
    def create(self, validated_data):
        img = ImgPremium.objects.create(image=validated_data.get('image'))
        return img
    class Meta:
        model = ImgPremium
        fields = ['image', 'id']

class ImgEnterpriseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField(required=True)
    def create(self, validated_data):
        img = ImgEnterprise.objects.create(image=validated_data.get('image'))
        return img
    class Meta:
        model = ImgEnterprise
        fields = ['image', 'id']
