from cProfile import label
from django import forms

class SettingsForm(forms.Form):

    site_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Название сайта',
        required=False,
    )
    site_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Описание сайта',
        required=False,
    )
    logo = forms.CharField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Логотип',
        required=False,
    )
    favicon = forms.CharField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Фавикон',
        required=False,
    )
    head = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Текст в блоке head',
        required=False,
    )
    footer = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Текст в подвале сайта',
        required=False,
    )
    is_show_count_of_post_in_rubrics = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
            }
        ),
        label='Показывать количество записей в рубриках',
        required=False,
    )