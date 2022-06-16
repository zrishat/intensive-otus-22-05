"""
templatetags
"""


from django import template


register = template.Library()


@register.simple_tag
def total_cost(price, persons_count=1):
    return price * persons_count
