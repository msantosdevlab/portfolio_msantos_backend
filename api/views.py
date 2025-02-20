from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import translation
from .models import Menu, Introduction, ProjectSectionContent, ProjectCategory, Project, Linkedin, Contact, Footer
from .serializers import (
    MenuSerializer,
    IntroductionSerializer,
    ProjectSectionContentSerializer,
    ProjectCategorySerializer,
    ProjectSerializer,
    LinkedinSerializer,
    ContactSerializer,
    FooterSerializer
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

class TokenObtainAccessOnlyView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)  # Chama o método da classe pai
        # Aqui você pode manipular a resposta para retornar apenas o access token
        response.data = {'access': response.data['access']}
        return response

class ContentViewSet(ReadOnlyModelViewSet):
    # Valida o token em cada requisição
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        # Obtém o idioma da requisição (parâmetro 'lang' da URL)
        lang = request.GET.get('lang', 'pt')  # Se não houver, usa 'pt' como idioma padrão
        translation.activate(lang)  # Ativa o idioma baseado no parâmetro 'lang'

        # Busca os dados do modelo e serializa conforme o idioma
        menu = Menu.objects.all()
        menu_data = MenuSerializer(menu, many=True).data if menu else None

        introduction = Introduction.objects.first()
        introduction_data = IntroductionSerializer(introduction).data if introduction else None

        project_title = ProjectSectionContent.objects.first()
        project_title_data = ProjectSectionContentSerializer(project_title).data if project_title else None

        project_categories = ProjectCategory.objects.all()
        project_categories_data = ProjectCategorySerializer(project_categories, many=True).data if project_categories else None

        projects = Project.objects.all()
        projects_data = ProjectSerializer(projects, many=True).data if projects else None

        linkedin = Linkedin.objects.first()
        linkedin_data = LinkedinSerializer(linkedin).data if linkedin else None

        contact = Contact.objects.first()
        contact_data = ContactSerializer(contact).data if contact else None

        footer = Footer.objects.first()
        footer_data = FooterSerializer(footer).data if footer else None

        content_data = {
            'menu': menu_data,
            'introduction': introduction_data,
            'project_content': project_title_data,
            'project_categories': project_categories_data,
            'projects': projects_data,
            'linkedin': linkedin_data,
            'contact': contact_data,
            'footer': footer_data,
        }

        # Retorna a resposta com o conteúdo traduzido
        return Response(content_data, status=200)
