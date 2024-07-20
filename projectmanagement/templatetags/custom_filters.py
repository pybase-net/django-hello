from django import template

register = template.Library()


@register.filter(name='add_attr')
def add_attribute(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val

    return field.as_widget(attrs=attrs)


@register.filter(name='form_input_class')
def form_input_class(field, error=None):
    attrs = {'class': 'form-control'}
    if error:
        attrs['class'] += ' is-invalid'
    return field.as_widget(attrs=attrs)
