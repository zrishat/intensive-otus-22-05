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
    city = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите город',
                                                                        'id': 'city'})
                           )
    check_in = forms.DateField(label='Дата заезда',
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
                               # widget=DatePickerInput
                               )
    check_out = forms.DateField(label='Дата выезда',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
                                # widget=DatePickerInput
                                )
    amount_guests = forms.IntegerField(label='Гости', min_value=1, max_value=30,
                                       widget=forms.NumberInput(attrs={'class': 'form-control'}),
                                       initial=2)  # noqa: E501
