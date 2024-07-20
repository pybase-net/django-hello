from django.utils.translation import gettext_lazy as _

FIELDS = {
    # user
    'first_name': _('First name'),
    'last_name': _('Last name'),
    'password': _('Password'),
    'email': _('Email'),
}

GENERIC_ERRORS = {
    'required': _("%(field)s is required"),
    'invalid': _("%(field)s is invalid"),
    'unique': _("%(field)s is already in use"),
}

AUTH_REGISTER_SUCCESS = _('Congratulation, %(fullname)s! Your account has been created!')
