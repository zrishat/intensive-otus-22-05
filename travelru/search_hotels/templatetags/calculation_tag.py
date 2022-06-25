"""
templatetags
"""


from django import template


register = template.Library()


@register.simple_tag
def total_cost(price, nights, persons_count=1):
    """
    decorator simple tag
    """
    return price * nights * persons_count
