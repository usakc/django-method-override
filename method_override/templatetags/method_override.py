from __future__ import absolute_import

from django.template import Library
from django.utils.safestring import mark_safe

from method_override import settings


__all__ = ['method_override']


register = Library()


@register.simple_tag
def method_override(method):
    '''Renders a hidden input with the method override value.'''
    input = settings.INPUT_TEMPLATE.format(
        name=settings.PARAM_KEY, value=method
    )
    return mark_safe(input)
