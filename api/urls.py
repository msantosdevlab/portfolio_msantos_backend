from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, TokenObtainAccessOnlyView


router = DefaultRouter()
router.register(r'content', ContentViewSet, basename='content')

urlpatterns = [
    path('', include(router.urls)),
    path('token/access/', TokenObtainAccessOnlyView.as_view(), name='token_obtain_access_only'),
]
