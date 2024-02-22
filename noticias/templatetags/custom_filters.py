from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter(name='domain_only')
def domain_only(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc
