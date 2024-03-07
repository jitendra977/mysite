from django.http import HttpResponse
from django.shortcuts import redirect, render

from vegapp.form import EditForm, AddForm

from .models import Recipe

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/vegapp/')  # Redirect to a success page
    else:
        form = AddForm()

    queryset = Recipe.objects.all()
    context = {'recipe':queryset}
    return render (request,'index.html',context)
# add item
def add_recipe(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/vegapp/')  # Redirect to a success page
    else:
        form = AddForm()

    queryset = Recipe.objects.all()
    context = {'recipe':queryset}
    
    return render(request, 'add_recipe.html', {'form': form})
  

# delete item
def delete_recipe(request, id):
    recipe = Recipe.objects.filter(id=id).first()
    if recipe:
        recipe.delete()
    return redirect('/vegapp/')

# edit item
def edit_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('/vegapp/')
    else:
        form = EditForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})
  