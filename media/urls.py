from django.urls import path

from media.views import ListImagesThumbnails, ImgPremiumViewSet, ImgBasicViewSet, ImgEnterpriseViewSet
from rekrutacja.urls import router

urlpatterns = [
    path('listimgpremium', ListImagesThumbnails.as_view()),

]
urlpatterns += router.urls
router.register(
    r'imgbasic',
    ImgBasicViewSet,
    basename='basic',
)
router.register(
    r'imgpremium',
    ImgPremiumViewSet,
    basename='premium'
)
router.register(
    r'imgenterprise',
    ImgEnterpriseViewSet,
    basename='enterprise'
)

