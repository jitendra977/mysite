from ast import mod
from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe/")
    
    # def update_recipe(self, name, description, image):
    #     self.recipe_name = name
    #     self.recipe_description = description
    #     self.recipe_image = image
    #     self.save()