from django import forms

from media.models import Img


class ImageForm(forms.ModelForm):

    class Meta:
        model = Img
        fields = ['image']

    def clean_image(self):
        self.image = self.cleaned_data.get('image', False)

    def send_image(self):
        Img.objects.create(image=self.image)
