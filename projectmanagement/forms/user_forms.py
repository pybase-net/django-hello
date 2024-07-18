from django import forms
# from django.utils.translation import gettext as _
from .utils import format_form_validation_errors


class RegisterForm(forms.Form):
    email = forms.EmailField(
        max_length=254,

    )
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    password = forms.CharField(min_length=6, max_length=60)

    def process_form_data(self):
        if self.is_valid():
            """
            Extract and processed the cleaned data from the register form.            
            """
            email = self.cleaned_data['email']
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            password = self.cleaned_data['password']

            return None, {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password}
        # default return errors
        return format_form_validation_errors(self.errors), None
