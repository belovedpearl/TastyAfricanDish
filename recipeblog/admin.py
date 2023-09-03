from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'post_approved', 'date_created')
    search_fields = ['title', 'cook_time']   # 'country', 
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('date_created','post_approved')  # , 'country'
    summernote_fields = ('ingredients', 'instructions')
