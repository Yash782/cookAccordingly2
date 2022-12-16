from django.shortcuts import render
from .models import Ingredients, Recipes
from django.db.models import Q
# Create your views here.

def index(request):

    # To fetch all the ingredients from database
    ings = Ingredients.objects.all()

    # Code for searching Recipes by name on index page
    if 'q' in request.GET:
        q = request.GET['q']
        recs = Recipes.objects.filter (Q(Rname__icontains=q))

        # Redirect to recipe page with searched recipe
        return render(request, 'recipes.html', {'recs': recs})

    # Display list of selected ingredients by user
    if request.method == 'POST':
        selectedIngs = request.POST.getlist('selectedIngs')
        print(selectedIngs)

        recipes = Recipes.objects.filter(Iname__in=selectedIngs)

        # Print the names of the matching recipes
        for recipe in recipes:
            print(recipe.Rname)

        # Temporayly returing to home page even after selecting ingridents
        # Have to change to recipe page
        return render(request, 'index.html', {'ings': ings})
        
    return render(request, 'index.html', {'ings' : ings})

def recipes(request):

    #To Fetch all the recipes from database
    recs = Recipes.objects.all()

    # To search for recipes from recipes page
    if 'q' in request.GET:
        q = request.GET['q']
        recs = Recipes.objects.filter (Q(name__icontains=q)) 
    
    return render(request, 'recipes.html', {'recs': recs})


def singlerecipe(request):
    return render(request, 'single-recipe.html')