from django.shortcuts import render
from django.views import generic
from .models import Recipe


class RecipeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(post_approved=True).order_by('-date_created')
    template_name = "index.html"
    paginate_by = 8

class RecipeDetails(generic.DetailView,):
    model = Recipe
    template_name = "details.html"
