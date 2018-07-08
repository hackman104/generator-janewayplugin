from django import forms

class <%= shortName %>AdminForm(forms.Form):
    <%= shortName %>_enabled = forms.BooleanField(required=False)