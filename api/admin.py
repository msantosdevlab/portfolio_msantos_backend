from django.contrib import admin
from .models import Introduction, ProjectSectionTitle, ProjectCategory, TechStack, Project

# Registro do modelo Introduction
@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ("eyebrow", "title", "description")

    def has_add_permission(self, request):
        # Limita a quantidade de registros para um
        return not Introduction.objects.exists()

# Registro do modelo ProjectSectionTitle
@admin.register(ProjectSectionTitle)
class ProjectSectionTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

    def has_add_permission(self, request):
        # Limita a quantidade de registros para um
        return not ProjectSectionTitle.objects.exists()

# Registro do modelo ProjectCategory
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

# Registro do modelo TechStack
@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Registro do modelo Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_left', 'link_rep_git', 'link_preview')
    search_fields = ('title', 'description_left', 'link_rep_git', 'link_preview')
    filter_horizontal = ('techs',)
