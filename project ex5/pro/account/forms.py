from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password1","password2"]

class LogForm(forms.Form) :
    uname=forms.CharField(max_length=100,label="Enter UserName",widget=forms.TextInput(attrs={"class":"form-control"}))  
    pswd=forms.CharField(max_length=100,label="Enter Password",widget=forms.TextInput(attrs={"class":"form-control"}))            
