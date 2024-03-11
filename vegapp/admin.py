from django.contrib import admin

from vegapp.models import Recipe
class ShowRecipe(admin.ModelAdmin):
    list_display = ('recipe_name','recipe_description',)
# Register your models here.
admin.site.register(Recipe,ShowRecipe)