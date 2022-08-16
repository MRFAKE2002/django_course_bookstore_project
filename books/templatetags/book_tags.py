from django import template

register = template.Library()

@register.filter
def customtemplatetags(value):
    pass