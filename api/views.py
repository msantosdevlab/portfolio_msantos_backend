from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Introduction
from .serializers import IntroductionSerializer

class APIKeyPermission(BasePermission):
    def has_permission(self, request, view):
        auth = JWTAuthentication()
        header = auth.get_header(request)
        if not header:
            return False
        try:
            token = auth.get_raw_token(header)
            validated_token = auth.get_validated_token(token)
            return True
        except AuthenticationFailed:
            return False

class IntroductionViewSet(ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [APIKeyPermission]
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({}, status=204)

