from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeView.as_view(), name='home'),
]