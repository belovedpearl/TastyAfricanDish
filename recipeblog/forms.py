from .models import Recipe, Country
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field



class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter country name'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Form helper to generate form fields
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),     
            Submit('submit', 'Submit', css_class='btn btn-secondary btn-lg', style='margin-bottom: 10px;')
        )


""" Get the available list in the country model """
choices = Country.objects.all().values_list('name', 'name')
country_list = []
for choice in choices:
    country_list.append(choice)



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'author', 'description', 'country', 'ingredients', 'instructions', 'recipe_image', 'cook_time',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Recipe Local Name'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(choices=country_list, attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control'}),
            'instruction': forms.Textarea(attrs={'class': 'form-control'}),
            'cook_time': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'placeholder':'in minutes'}),
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
            Field('country'),
            Field('ingredients'),
            Field('instructions'),
            Field('recipe_image'),
            Field('cook_time'),
            Submit('submit', 'Submit', css_class='btn btn-secondary btn-lg', style='margin-bottom: 10px;')
        )


