from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe


class RecipeView(ListView):
    model = Recipe
    queryset = Recipe.objects.filter(post_approved=True).order_by('-date_created')
    template_name = "index.html"
    paginate_by = 8
