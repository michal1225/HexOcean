
from django.urls import path

from media.views import ImageFormView



urlpatterns = [

    path('', ImageFormView.as_view(success_url="/success/")),

]

