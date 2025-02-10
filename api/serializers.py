from rest_framework import serializers
from .models import Introduction, ProjectSectionTitle, ProjectCategory, TechStack, Project
from django.core.exceptions import ValidationError

class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'

class ProjectSectionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSectionTitle
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