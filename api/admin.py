from django.contrib import admin
from .models import Introduction, ProjectSectionTitle, ProjectsSectionCategories, ProjectCardTag, ProjectCard

# Register your models here.
@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ("eyebrow", "title", "description")

    def has_add_permission(self, request):
        # Limita a quantidade de regisro pra um
        return not Introduction.objects.exists()


@admin.register(ProjectSectionTitle)
class ProjectSectionTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

    def has_add_permission(self, request):
        # Limita a quantidade de regisro pra um
        return not ProjectSectionTitle.objects.exists()
    
@admin.register(ProjectsSectionCategories)
class ProjectsSectionCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

# Registro do modelo ProjectCardTag
@admin.register(ProjectCardTag)
class ProjectCardTagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Exibe o nome da tag na listagem

# Registro do modelo ProjectCard
@admin.register(ProjectCard)
class ProjectCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link_rep_git', 'link_preview')
    filter_horizontal = ('tags',)
    search_fields = ('title', 'description', 'link_rep_git', 'link_preview')
    