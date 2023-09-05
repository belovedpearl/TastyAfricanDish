from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeView.as_view(), name='home'),
    path('details/<slug:slug>', views.RecipeDetails.as_view(), name='recipe-detail'),
    path('addrecipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('updaterecipe/edit/<slug:slug>', views.UpdateRecipe.as_view(), name='updaterecipe'),

]