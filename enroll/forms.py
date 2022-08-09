from django import forms
from .models import User

class StudentRegis(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        # widgets = {
        #     'name':forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.EmailField(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }
        