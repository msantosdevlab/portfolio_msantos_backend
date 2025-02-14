from rest_framework import serializers
from .models import Menu, Introduction, ProjectSectionContent, ProjectCategory, TechStack, Project, Linkedin, Contact, Footer

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'

class ProjectSectionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSectionContent
        fields = '__all__'

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)  # Exibe o nome da categoria
    techs = TechStackSerializer(many=True, read_only=True)  # Serializa a relação many-to-many com TechStack
    thumbnail = serializers.ImageField(max_length=200)  # Serializa o campo de imagem

    class Meta:
        model = Project
        fields = '__all__'

    def validate_img(self, value):
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("The file is too big. The limit is 5MB.")
        return value
    
class LinkedinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linkedin
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'