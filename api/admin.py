from django.contrib import admin
from .models import Introduction, ProjectSectionTitle, ProjectCategory, TechStack, Project, Linkedin, Contact

LANGUAGE_SUFFIXES = ("_pt", "_es", "_en")

def filter_translatable_fields(model):
    """Filtra os campos que possuem sufixos de idioma."""
    return [field.name for field in model._meta.fields if field.name.endswith(LANGUAGE_SUFFIXES)]

# Registro do modelo Introduction
@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ("eyebrow", "title", "description")

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)

    def has_add_permission(self, request):
        return not Introduction.objects.exists()

# Registro do modelo ProjectSectionTitle
@admin.register(ProjectSectionTitle)
class ProjectSectionTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)

    def has_add_permission(self, request):
        return not ProjectSectionTitle.objects.exists()

# Registro do modelo ProjectCategory
@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)


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

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)

# Registro do modelo Linkedin
@admin.register(Linkedin)
class LinkedinAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)

    def has_add_permission(self, request):
        return not Linkedin.objects.exists()

# Registro do modelo Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)

    def has_add_permission(self, request):
        return not Contact.objects.exists()
