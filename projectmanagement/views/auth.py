from django.shortcuts import render
from ..forms import RegisterForm
from ..models import User


def auth_register(request):
    is_post_request = request.method == 'POST'
    errors, data = None, None
    if is_post_request:
        # validate form data
        form = RegisterForm(request.POST)
        errors, data = form.process_form_data()
    return render(request, 'auth/register.html', {
        'errors': errors,
        'data': data,
        'is_post_request': is_post_request
    })


def auth_login(request):
    return render(request, 'auth/login.html')
