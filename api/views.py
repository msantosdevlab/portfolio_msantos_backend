from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Introduction, ProjectSectionTitle, ProjectCategory, Project, Linkedin, Contact
from .serializers import (
    IntroductionSerializer,
    ProjectSectionTitleSerializer,
    ProjectCategorySerializer,
    ProjectSerializer,
    LinkedinSerializer,
    ContactSerializer
)
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
        introduction = Introduction.objects.first()
        introduction_data = IntroductionSerializer(introduction).data if introduction else None

        project_title = ProjectSectionTitle.objects.first()
        project_title_data = ProjectSectionTitleSerializer(project_title).data if project_title else None

        project_categories = ProjectCategory.objects.all()
        project_categories_data = ProjectCategorySerializer(project_categories, many=True).data if project_categories else None

        projects = Project.objects.all()
        projects_data = ProjectSerializer(projects, many=True).data if projects else None

        linkedin = Linkedin.objects.first()
        linkedin_data = LinkedinSerializer(linkedin).data if linkedin else None

        contact = Contact.objects.first()
        contact_data = ContactSerializer(contact).data if contact else None

        content_data = {
            'introduction': introduction_data,
            'project_title': project_title_data,
            'project_categories': project_categories_data,
            'projects': projects_data,
            'linkedin': linkedin_data,
            'contact': contact_data,

        }

        return Response(content_data, status=200)
