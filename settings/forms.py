from django import forms

class SettingsForm(forms.Form):

    site_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Название сайта'
    )
    site_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Описание сайта'
    )
    logo = forms.CharField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Логотип'
    )
    favicon = forms.CharField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Фавикон '
    )
    head = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Текст в блоке head'
    )
    footer = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        ),
        label='Текст в подвале сайта'
    )