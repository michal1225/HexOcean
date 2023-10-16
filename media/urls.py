from django.urls import path

from media.views import ListImagesThumbnails
from rekrutacja.urls import router

urlpatterns = [
    path('listimg', ListImagesThumbnails.as_view()),

]



