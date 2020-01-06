from django import forms
from testapp.models import comment
class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields=('name','body')
