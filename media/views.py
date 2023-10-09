from django.views.generic import FormView

from media.forms import ImageForm


class ImageFormView(FormView):
    form_class = ImageForm
    template_name = "sendImage.html"

    def form_valid(self, form):
        form.send_image()
        return super().form_valid(form)
