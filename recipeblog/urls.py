from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeView.as_view(), name='home'),
    path('details/<slug:slug>', views.RecipeDetails.as_view(), name='recipe-detail'),

]