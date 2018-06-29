from django import forms
from projectDB.models import Profile

class NameForm(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=100)
    city = forms.CharField(label='Your city', max_length=100)
    country = forms.CharField(label='Your country', max_length=100)
    phoneno = forms.IntegerField(label='Your phone')

    class Meta:
        model = Profile
        fields = ('name','city','country','phoneno',)
