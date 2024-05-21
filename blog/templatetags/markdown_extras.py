import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_to_html(value):
    return mark_safe(markdown.markdown(value,extensions=['extra','codehilite','toc']))