from django.db import models
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
from modeltranslation.translator import TranslationOptions

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
    
class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, unique=True) # Para controlar a ordem de exibição

    def __str__(self):
        return self.label
    
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

class Introduction(models.Model):
    eyebrow = models.CharField(max_length=65, blank=True, null=True)
    title = models.CharField(max_length=65, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    button_text = models.CharField(max_length=165, blank=True, null=True)
    button_href = models.CharField(max_length=200, choices=TARGET_BTN, default="_self")

    def __str__(self):
        return f"{str(self.title)[:50]}"
    
    class Meta:
        verbose_name = "Introduction"
        verbose_name_plural = "Introduction"

class ProjectSectionContent(models.Model):
    title = models.CharField(max_length=65, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    text_link_preview = models.CharField(max_length=255, blank=True, null=True)
    text_btn_detail = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{str(self.title)[:50]}"
    
    class Meta:
        verbose_name = "Project Section Content"
        verbose_name_plural = "Project Section Content"

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{str(self.name)}"
    
    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

class TechStack(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{str(self.name)}"
    
    class Meta:
        verbose_name = "Tech Stack"
        verbose_name_plural = "Tech Stacks"


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
    title = HTMLField(max_length=65, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    button_href = models.CharField(max_length=165, blank=True, null=True)
    button_text = models.CharField(max_length=165, blank=True, null=True)
    button_target = models.CharField(max_length=200, choices=TARGET_BTN, default="_self")

    def __str__(self):
        return f"{str(self.title)[:50]}"
    
    class Meta:
        verbose_name = "Linkedin"
        verbose_name_plural = "Linkedin"
    

class Contact(models.Model):
    title = models.CharField(max_length=65, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    button_href = models.CharField(max_length=165, blank=True, null=True)
    button_text = models.CharField(max_length=165, blank=True, null=True)
    button_target = models.CharField(max_length=200, choices=TARGET_BTN, default="_self")

    def __str__(self):
        return f"{str(self.title)[:50]}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"
    
class Footer(models.Model):
    text = models.CharField(max_length=255, unique=True)
    icon_href = models.CharField(max_length=165, blank=True, null=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

class MenuTranslationOptions(TranslationOptions):
    fields = ('label', )

class IntroductionTranslationOptions(TranslationOptions):
    fields = ('eyebrow', 'title', 'description', 'button_text')

class ProjectSectionContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text_link_preview', 'text_btn_detail')

class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description_right', 'description_left')
   
class LinkedinTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_text')

class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'button_text')

class FooterTranslationOptions(TranslationOptions):
    fields = ('text',)