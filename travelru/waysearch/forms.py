"""
forms
"""
from datetime import datetime

from django import forms


class WaysearchForm(forms.Form):
    """
    Avia tickets search
    """
    today_date = datetime.today().strftime("%Y-%m-%d")
    departure_city = forms.CharField(
        label='Откуда',
        widget=forms.TextInput(
            attrs={'class': 'city-auto form-control', 'placeholder': 'Откуда'}
        )
    )
    arrival_city = forms.CharField(
        label='Куда',
        widget=forms.TextInput(
           attrs={'class': 'city-auto form-control', 'placeholder': 'Куда'}
        )
    )
    departure_date = forms.DateField(
        label='Дата вылета',
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control', 'min': today_date}
        )
    )
    arrival_date = forms.DateField(
        label='Дата обратно',
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control', 'min': today_date}
        )
    )
