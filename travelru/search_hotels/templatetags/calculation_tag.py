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


@register.simple_tag
def print_multiple(value, count):
    """Print a value multiple times."""
    return ' '.join([value] * count)

@register.filter(name='times')
def times(number):
    return range(number)