from rest_framework import serializers
from .models import Introduction, ProjectSectionTitle, ProjectsSectionCategories, ProjectCardTag, ProjectCard

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

# Serializer ProjectCardTag
class ProjectCardTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCardTag
        fields = ['name']

# Serializer ProjectCard
class ProjectCardSerializer(serializers.ModelSerializer):
    tags = ProjectCardTagSerializer(many=True, read_only=True)  # Relacionamento muitos-para-muitos com tags

    class Meta:
        model = ProjectCard
        fields = ['title', 'img', 'description', 'tags', 'link_rep_git', 'link_preview']
        