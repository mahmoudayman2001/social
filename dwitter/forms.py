from django import forms
from .models import Dwitts

class DwittsForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
        attrs={
        "placeholder": "Dweet something...",
        "class": "textarea is-success is-medium",
        }
    ),
    label="",
)
    class Meta:
        model = Dwitts
        exclude = ("user", )