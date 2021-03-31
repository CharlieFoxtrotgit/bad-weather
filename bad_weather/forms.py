from django import forms

class QueryForm(forms.Form):
    location = forms.TextInput()
    start_date = forms.DateField()
    end_date = forms.DateField(required = False)