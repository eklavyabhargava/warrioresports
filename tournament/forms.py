from django import forms
from .models import tdm, classic

# creating a form
class tdmform(forms.ModelForm):
    # model to use
    class Meta:
        model = tdm
        fields = ("name", "email", "mobile_no", "pubg_id")

class classicform(forms.ModelForm):
    # model to use
    class Meta:
        model = classic
        fields = ("name", "email", "mobile_no", "pubg_id")