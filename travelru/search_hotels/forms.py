"""
forms
"""
from django import forms

# from search_hotels.widget import DatePickerInput


class SearchHotelsForm(forms.Form):
    """
    searchhotelsform
    """
    # city = forms.CharField(label='Город', initial='Введите город')
    city = forms.CharField(label='Город')
    check_in = forms.DateField(label='Дата заезда',
                               # widget=DatePickerInput
                               )
    check_out = forms.DateField(label='Дата выезда',
                                # widget=DatePickerInput
                                )
    amount_guests = forms.IntegerField(label='Гости', min_value=1, max_value=30)  # noqa: E501
