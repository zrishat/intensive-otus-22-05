"""
templatetags
"""
from django import template

from waysearch.templatetags.data_ru_airlines import data_ru_airlines

register = template.Library()


@register.simple_tag
def airline_translated(airline_code):
    """
    decorator simple tag
    """
    for airline in data_ru_airlines:
        if airline_code == airline['code']:
            if airline['name']:
                return airline['name']
            if airline['name_translations']['en']:
                return airline['name_translations']['en']
    return airline_code


@register.simple_tag
def formatted_depature(date_str):
    """
    decorator simple tag
    """
    date_day = date_str.split('T')[0].split('-')
    date_day = f"{date_day[2]}.{date_day[1]}.{date_day[0]}"
    date_time = date_str.split('T')[1].split('+')[0]
    return f"Дата: {date_day}, Время: {date_time}"
