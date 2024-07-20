from django.shortcuts import render
from django.contrib import messages
from ..forms import RegisterForm
from ..models import User
from projectmanagement.translation import translation


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
        if data:
            u: User = User.objects.create_user(
                email=data['email'],
                username=User.generate_username(data['email']),
                password=data['password'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            messages.add_message(request, messages.SUCCESS,
                                 translation.AUTH_REGISTER_SUCCESS % {'fullname': u.full_name()})
            return render(request, 'auth/register_success.html', context)
    return render(request, 'auth/register.html', context)


def auth_login(request):
    return render(request, 'auth/login.html')
