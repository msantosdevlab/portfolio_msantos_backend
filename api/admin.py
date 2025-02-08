from django.contrib import admin
from .models import Introduction

# Register your models here.
@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ("eyebrow", "title", "description",)