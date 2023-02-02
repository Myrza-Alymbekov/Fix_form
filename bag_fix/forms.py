from django.forms import ModelForm, FileField, ClearableFileInput

from .models import Complaints


class ComplaintsForm(ModelForm):
    files = FileField(widget=ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Complaints
        fields = '__all__'
        read_only_fields = ['date']


