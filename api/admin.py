from django.contrib import admin
from .models import Introduction, ProjectSectionTitle

# Register your models here.
@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ("eyebrow", "title", "description",)

    def has_add_permission(self, request):
        # Limita a quantidade de regisro pra um
        return not Introduction.objects.exists()


@admin.register(ProjectSectionTitle)
class ProjectSectionTitleAdmin(admin.ModelAdmin):
    list_display = ("title", "description",)

    def has_add_permission(self, request):
        # Limita a quantidade de regisro pra um
        return not ProjectSectionTitle.objects.exists()