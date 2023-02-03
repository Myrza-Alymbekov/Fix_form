from django import forms
from django.forms import ModelForm, FileField, ClearableFileInput

from .models import Complaints


class ComplaintsForm(ModelForm):

    files = FileField(label="", widget=ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Complaints
        fields = ['name', 'text', 'importance']
        read_only_fields = ['date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Необязательное поле"}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'style': "margin-bottom: 30px;"}),
            # 'importance': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
        }

        labels = {
            'name': 'Вашe имя:',
            'text': 'Описание:',
            'importance': 'Срочность',
        }
