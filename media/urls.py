from django.urls import path

from media.views import ListImagesThumbnails, ImgViewSet
from rekrutacja.urls import router

urlpatterns = [
    path('listimg', ListImagesThumbnails.as_view()),

]
urlpatterns += router.urls
router.register(
    r'img',
    ImgViewSet,
    basename='basic',
)


