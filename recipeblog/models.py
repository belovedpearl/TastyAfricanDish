from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'DRAFTS'), (1, 'PUBLISHED'))


class Recipe(models.Model):
    """
    Recipe Model
    Meta put latest post first
    Generate count for the like button
    """
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_posts')
    slug = models.SlugField(max_length=150, unique=True) 
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    recipe_image = CloudinaryField('recipeimage', default='placeholder')
    cook_time = models.PositiveIntegerField()
    # country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countries')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_like', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

