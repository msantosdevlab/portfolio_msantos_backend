from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission  # ou sua APIKeyPermission personalizada
from rest_framework.exceptions import AuthenticationFailed
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

class ContentViewSet(ReadOnlyModelViewSet):
    # Valida o token em cada requisição
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    def list(self, request, *args, **kwargs):
        # Obtém a instância atualizada de Introduction a cada requisição
        introduction = Introduction.objects.first()
        introduction_data = IntroductionSerializer(introduction).data if introduction else None

        content_data = {
            'introduction': introduction_data,
        }

        return Response(content_data, status=200)
