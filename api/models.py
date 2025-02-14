from django.db import models
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError

TARGET_BTN = [
    ("_self", "_self"),
    ("_blank", "_blank"),
]

def validate_image(image):
    file_size = image.file.size
    limit_mb = 5  # Limitar o tamanho do arquivo para 5MB
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError(f"The file is too big. The limit is {limit_mb}MB.")

    file_extension = image.name.split('.')[-1].lower()
    valid_extensions = ['jpg', 'jpeg', 'png']
    if file_extension not in valid_extensions:
        raise ValidationError(f"Invalid image format. Only {', '.join(valid_extensions)} are allowed.")


class Introduction(models.Model):
    eyebrow = models.CharField(max_length=65, blank=True, null=True)
    title = models.CharField(max_length=65, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    button_text = models.CharField(max_length=165, blank=True, null=True)
    button_href = models.CharField(max_length=200, choices=TARGET_BTN, default="_self")

    def __str__(self):
        return f"{str(self.title)[:50]}"

class ProjectSectionTitle(models.Model):
    title = models.CharField(max_length=65, blank=True, null=True)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return f"{str(self.title)[:50]}"

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{str(self.name)}"

class TechStack(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{str(self.name)}"

class Project(models.Model):
    title = models.CharField(max_length=165, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='%Y-%m/%d/', validators=[validate_image])
    short_description = HTMLField(max_length=300, blank=True, null=True)
    description_right = HTMLField(blank=True, null=True)
    description_left = HTMLField(blank=True, null=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)  # Relação muitos-para-um
    techs = models.ManyToManyField(TechStack, blank=True) # Relação muitos-para-muitos
    link_rep_git = models.CharField(max_length=255, blank=True, null=True)
    link_preview = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{str(self.title)[:50]}"

class Linkedin(models.Model):
    title = HTMLField(max_length=95, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    button_href = models.CharField(max_length=165, blank=True, null=True)
    button_text = models.CharField(max_length=165, blank=True, null=True)
    button_target = models.CharField(max_length=200, choices=TARGET_BTN, default="_self")

    def __str__(self):
        return f"{str(self.title)[:50]}"
    

class Contact(models.Model):
    title = HTMLField(max_length=95, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    button_href = models.CharField(max_length=165, blank=True, null=True)
    button_text = models.CharField(max_length=165, blank=True, null=True)
    button_target = models.CharField(max_length=200, choices=TARGET_BTN, default="_self")

    def __str__(self):
        return f"{str(self.title)[:50]}"
