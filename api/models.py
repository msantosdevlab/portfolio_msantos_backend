from django.db import models
from ckeditor.fields import RichTextField

TARGET_BTN = [
    ("_self", "_self"),
    ("_blank", "_blank"),
]

class Introduction(models.Model):
    eyebrow = models.CharField(max_length=65, blank=True, null=True)
    title = models.CharField(max_length=65, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    button_text = models.CharField(max_length=165, blank=True, null=True)
    button_href = models.CharField(max_length=200, choices=TARGET_BTN, default="_self")

    def __str__(self):
        return f"{str(self.title)[:50]}"

class ProjectSectionTitle(models.Model):
    title = models.CharField(max_length=65, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{str(self.title)[:50]}"

class ProjectsSectionCategories(models.Model):
    name = models.CharField(max_length=65, blank=True, null=True)

    def __str__(self):
        return f"{str(self.name)}"
