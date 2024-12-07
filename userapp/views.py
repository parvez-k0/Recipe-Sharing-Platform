from django.shortcuts import render , redirect
from .models import *

# Create your views here.

def home(request):
    return render(request, "parent.html")

def foods(request):
    
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        
        Food.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image,
            )
        
        return redirect('/recipe-data/')
    
    queryset = Food.objects.all()
    
    return render(request, "recipes.html",  {'foods': queryset})

#to show your recipes data in another window

def recipe_data(request):
    queryset = Food.objects.all()
    
    return render(request , "recipe.html", {'foods': queryset})
    
    
def delete_food(request, id):
    queryset = Food.objects.get(id = id)
    queryset.delete()
    
    return redirect('/recipe-data/')
