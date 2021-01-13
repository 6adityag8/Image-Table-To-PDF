from django import template

register = template.Library()


@register.filter
def index(iterator, i):
    return iterator[i]
