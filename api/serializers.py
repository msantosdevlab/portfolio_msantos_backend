from rest_framework import serializers
from .models import Introduction, ProjectSectionTitle

class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'

# Serializer para ProjectSectionTitle
class ProjectSectionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSectionTitle
        fields = ['title', 'description']
