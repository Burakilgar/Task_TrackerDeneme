from django import forms
from .models import Task


class StudentForm(forms.ModelForm):
   
    class Meta:
        model = Task
        fields = ["task", "day"]
        widgets = {
            'task': forms.TextInput(attrs={'placeholder': 'Task'}),
            'day': forms.TextInput(
                attrs={'placeholder': 'Time &Day'}),
        }
   