from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Introduction, ProjectSectionTitle, ProjectsSectionCategories,ProjectCardTag, ProjectCard
from .serializers import IntroductionSerializer, ProjectSectionTitleSerializer, ProjectsSectionCategoriesSerializer, ProjectCardTagSerializer, ProjectCardSerializer

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

        project_title = ProjectSectionTitle.objects.first()
        project_title_data = ProjectSectionTitleSerializer(project_title).data if project_title else None

        project_categories = ProjectsSectionCategories.objects.all()
        project_categories_data = ProjectsSectionCategoriesSerializer(project_categories, many=True).data if project_categories else None

        project_cards = ProjectCard.objects.all()
        project_cards_data = ProjectCardSerializer(project_cards, many=True).data if project_cards else None

        # Obtém todos os registros de ProjectCardTag
        project_card_tags = ProjectCardTag.objects.all()
        project_card_tags_data = ProjectCardTagSerializer(project_card_tags, many=True).data if project_card_tags else None

        content_data = {
            'introduction': introduction_data,
            'project_title': project_title_data,
            'project_categories': project_categories_data,
            'project_cards': project_cards_data,
            'project_card_tags': project_card_tags_data,
        }

        return Response(content_data, status=200)
