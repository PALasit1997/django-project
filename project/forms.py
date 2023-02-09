from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


            #--:signup page:--
# class user_form(forms.Form):
#     username = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}),max_length=50)
#     password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),max_length=50)
#     first_name = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}), max_length=100)
#     last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), max_length=100)
#     email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}),max_length=100)

class signup(UserCreationForm):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # email = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")
        labels = {"email":"Email"}
    
    # def save(self,commit=True):
    #     Students = super(signup,self).save(commit=False)
    #     Students.first_name  = self.cleaned_data[first_name]
    #     Students.last_name  = self.cleaned_data[last_name]
    #     Students.email  = self.cleaned_data[email]
    
    #     if commit:
    #         Students.save()
    #     return Students


        # --:login page:--
class login_form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)