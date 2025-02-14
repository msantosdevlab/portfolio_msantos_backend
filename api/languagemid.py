from django.utils import translation

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obtém o parâmetro 'lang' da URL
        lang = request.GET.get('lang')
        if lang:
            translation.activate(lang)  # Ativa o idioma baseado no parâmetro 'lang'
        else:
            translation.activate('pt')  # Idioma padrão

        response = self.get_response(request)
        return response
