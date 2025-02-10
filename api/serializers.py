from rest_framework import serializers
from .models import Introduction, ProjectSectionTitle, ProjectsSectionCategories

class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'

# Serializer ProjectSectionTitle
class ProjectSectionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSectionTitle
        fields = ['title', 'description']

# Serializer ProjectsSectionCategories
class ProjectsSectionCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsSectionCategories
        fields = ['name']