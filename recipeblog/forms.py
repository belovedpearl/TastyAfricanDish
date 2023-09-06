from .models import Recipe
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'author', 'description', 'ingredients', 'instructions', 'recipe_image', 'cook_time',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Recipe Local Name'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'instruction': forms.Textarea(attrs={'class': 'form-control'})       
            
        }

    def __init__(self, *args, **kwargs):
        """
        Form helper to generate form fields
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title'),
            Field('author'),
            Field('description'),
            Field('ingredients'),
            Field('instructions'),
            Field('recipe_image'),
            Field('cook_time'),
            Submit('submit', 'Submit', css_class='btn btn-secondary btn-lg')
        )
