"""Forms of the project."""
from django import forms
from .models import Thing
# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(attrs={'maxlength': 120}),
            'quantity': forms.NumberInput(),
            'name': forms.TextInput(attrs={'maxlength': 35})
        }

