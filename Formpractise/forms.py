from django import  forms
from .models import  Student


class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
                'dateofBirth': forms.DateInput(attrs={'type':'date'})
        }