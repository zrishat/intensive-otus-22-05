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
    # print(type(price), type(nights), type(persons_count))
    return price * nights * persons_count
