from django.shortcuts import render
from ..forms import RegisterForm
from ..models import User


def auth_register(request):
    is_post_request = request.method == 'POST'
    context = {
        'is_post_request': is_post_request,
        'errors': None,
        'data': None,
    }
    form = RegisterForm(request.POST) if is_post_request else RegisterForm()
    context['form'] = form
    context['field_names'] = RegisterForm.get_field_names()
    if is_post_request:
        # validate form data
        errors, data = form.process_form_data()
        context['errors'] = errors
        context['data'] = data
    return render(request, 'auth/register.html', context)


def auth_login(request):
    return render(request, 'auth/login.html')
