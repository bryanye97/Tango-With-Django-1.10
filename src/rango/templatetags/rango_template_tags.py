from django import template
from rango.categories import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
