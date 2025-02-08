from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IntroductionViewSet

router = DefaultRouter()
router.register(r'introduction', IntroductionViewSet, basename='introduction')

urlpatterns = [
    path('', include(router.urls)),
]
