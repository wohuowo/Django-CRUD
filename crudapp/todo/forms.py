from django import forms
from .models import TodoApp #this dot means in the current directory from insiide the model file import TodoApp

class TodoAppForm(forms.ModelForm):
    #creating a meta class
    class Meta:
        #specifying model to be used on our forms
        model = TodoApp

        #specifying fields to be used. what should be show on the form
        fields = [
            "title",
            "description",
        ]
