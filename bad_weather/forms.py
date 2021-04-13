from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class QueryForm(forms.Form):
    location = forms.CharField()
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget=forms.SelectDateWidget, required = False)
    desired_weather = forms.CharField()


class RegisterForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)