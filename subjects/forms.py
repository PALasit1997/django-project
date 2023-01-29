from django import forms
form subject.models import subject


class subjectform(forms.ModelForm):
    class Meta:
        models  = subjects
        fields = "__all__"
