from django import forms

from .models import BarsLocation

class BarsCreateForm(forms.Form):
    name            = forms.CharField()
    location        = forms.CharField(required=False)
    category        = forms.CharField(required=False)

    # custom way of validating the data
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

class BarsLocationCreateForm(forms.ModelForm):
    class Meta:
        model = BarsLocation
        fields = [
            'name',
            'location',
            'category'
        ]
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
