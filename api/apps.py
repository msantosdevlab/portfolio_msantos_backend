from django.apps import AppConfig
from modeltranslation.translator import translator

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Registra as traduções somente quando os modelos estiverem carregados
        from .models import Introduction, ProjectCategory, Project, Linkedin, Contact
        from .models import IntroductionTranslationOptions, ProjectCategoryTranslationOptions, ProjectTranslationOptions, LinkedinTranslationOptions, ContactTranslationOptions
        translator.register(Introduction, IntroductionTranslationOptions)
        translator.register(ProjectCategory, ProjectCategoryTranslationOptions)
        translator.register(Project, ProjectTranslationOptions)
        translator.register(Linkedin, LinkedinTranslationOptions)
        translator.register(Contact, ContactTranslationOptions)
