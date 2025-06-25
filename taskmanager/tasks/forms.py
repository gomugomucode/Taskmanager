from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class CustomLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md text-sm',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md text-sm',
            'placeholder': 'Password'
        })
    )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md text-sm',
            'placeholder': 'Email'
        })
    )

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = ''
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm',
                'placeholder': field.label,
            })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Task title'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3, 'placeholder': 'Task description'}),
            'completed': forms.CheckboxInput(attrs={'class': 'mr-2'}),
            'due_date': forms.DateInput(attrs={'class': 'w-full p-2 border rounded', 'type': 'date'}),
        }

