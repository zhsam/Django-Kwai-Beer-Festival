from django import forms

from .models import BarsLocation
from .validators import validate_category

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
    #category            = forms.CharField(required=False,validators=[validate_category])
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
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if ".edu" in email:
    #         raise forms.ValidationError("We do not accept edu email")
    #     return email
