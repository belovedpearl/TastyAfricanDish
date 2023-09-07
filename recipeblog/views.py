from django.shortcuts import render
from django.views import generic
from .models import Recipe
from .forms import RecipeForm
from django.urls import reverse_lazy


class RecipeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(post_approved=True).order_by('-date_created')
    template_name = "index.html"
    paginate_by = 8


class RecipeDetails(generic.DetailView,):
    model = Recipe
    template_name = "details.html"


class AddRecipe(generic.CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "addrecipe.html"


class UpdateRecipe(generic.UpdateView):
    model = Recipe
    template_name = "updaterecipe.html"
    form_class = RecipeForm
  
    
class DeleteRecipe(generic.DeleteView):
    model = Recipe
    template_name = "deleterecipe.html"
    success_url = reverse_lazy('home')
