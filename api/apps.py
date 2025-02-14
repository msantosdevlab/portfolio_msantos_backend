from django.apps import AppConfig
from modeltranslation.translator import translator

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Registra as traduções somente quando os modelos estiverem carregados
        from .models import Menu, Introduction, ProjectSectionContent, ProjectCategory, Project, Linkedin, Contact, Footer
        from .models import MenuTranslationOptions, IntroductionTranslationOptions, ProjectSectionContentTranslationOptions, ProjectCategoryTranslationOptions, ProjectTranslationOptions, LinkedinTranslationOptions, ContactTranslationOptions, FooterTranslationOptions
        translator.register(Menu, MenuTranslationOptions)
        translator.register(Introduction, IntroductionTranslationOptions)
        translator.register(ProjectSectionContent, ProjectSectionContentTranslationOptions)        
        translator.register(ProjectCategory, ProjectCategoryTranslationOptions)
        translator.register(Project, ProjectTranslationOptions)
        translator.register(Linkedin, LinkedinTranslationOptions)
        translator.register(Contact, ContactTranslationOptions)
        translator.register(Footer, FooterTranslationOptions)
