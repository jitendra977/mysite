# forms.py
from django import forms
from .models import Recipe

class AddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_description', 'recipe_image']
        widgets = {
            'recipe_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),  # Add Bootstrap form-control class
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),  # Add Bootstrap form-control class
            'recipe_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Add Bootstrap form-control class
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_description', 'recipe_image']
        widgets = {
            'recipe_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),  # Add Bootstrap form-control class
            'recipe_name': forms.TextInput(attrs={'class': 'form-control'}),  # Add Bootstrap form-control class
            'recipe_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Add Bootstrap form-control class
        }
