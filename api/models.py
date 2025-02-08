from django.db import models
from django.contrib.auth.models import User

class Introduction(models.Model):
    TARGET_BTN = [
        ("_blank", "_blank"),
        ("_self", "_self"),
    ]

    eyebrow = models.CharField(max_length=65, default=False, blank=True, null=True)
    title = models.CharField(max_length=65, default=False, blank=True, null=True)
    description = models.TextField(default=False, blank=True, null=True)
    button_text = models.CharField(max_length=165, default=False, blank=True, null=True)
    button_icon = models.CharField(max_length=65, default=False, blank=True, null=True)
    button_href = models.CharField(max_length=200, default=False, blank=True, null=True)

    def __str__(self):
        return f"{str(self.title)[:50]}"
    
