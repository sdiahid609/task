from django import forms

from .models import Task

#class TaskForm(forms.ModelForm):
#
#    class Meta:
#        model = Task
#       fields = ('title', 'description',)


class TaskForm(forms.Form):
    title = forms.CharField(label="Introduce el título", max_length=100)
    description = forms.CharField(label="Introduce la descripción", widget=forms.Textarea)
    checkBox = forms.BooleanField(label="¿Esta realizada?", required=False)
