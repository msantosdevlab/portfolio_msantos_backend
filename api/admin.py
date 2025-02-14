from django.contrib import admin
from .models import Menu, Introduction, ProjectSectionContent, ProjectCategory, TechStack, Project, Linkedin, Contact, Footer

LANGUAGE_SUFFIXES = ("_pt", "_es", "_en")

def filter_translatable_fields(model):
    """Filtra os campos que possuem sufixos de idioma."""
    return [field.name for field in model._meta.fields if field.name.endswith(LANGUAGE_SUFFIXES)]

# Registro do modelo Menu
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "label_pt", "label_es", "label_en")
    
    fieldsets = (
        (None, {
            'fields': ('name', 'order')  # Exibe os campos 'name' e 'order'
        }),
        ('Traduções', {
            'fields': ('label_pt', 'label_es', 'label_en'),
        }),
    )

# Registro do modelo Introduction
@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ("eyebrow", "title", "description")

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)

    def has_add_permission(self, request):
        return not Introduction.objects.exists()

# Registro do modelo ProjectSectionContent
@admin.register(ProjectSectionContent)
class ProjectSectionContentAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "text_link_preview", "text_btn_detail")

    def get_fields(self, request, obj=None):
        return filter_translatable_fields(self.model)

    def has_add_permission(self, request):
        return not ProjectSectionContent.objects.exists()

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
    
# Registro do modelo Contact
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("text", "icon_href")
    
    fieldsets = (
        (None, {
            'fields': ('icon_href',) 
        }),
        ('Traduções', {
            'fields': ('text_pt', 'text_es', 'text_en'),
        }),
    )

    def has_add_permission(self, request):
        return not Footer.objects.exists()



