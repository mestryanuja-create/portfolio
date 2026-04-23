from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'role', 'description', 'technologies', 'clients', 'image']
    image = forms.ImageField(label='Project Image', required=False)