from django.shortcuts import redirect
from django.utils import translation
from django.conf import settings


def switch_language(request, language_code):
    next_url = request.GET.get('next', '/')
    response = redirect(next_url)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
    translation.activate(language_code)
    return response
