from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'gender', 'phone']
        widgets = {
            'gender': forms.Select(choices=Student.GENDER_CHOICES),
        }
