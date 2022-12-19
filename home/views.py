from django.shortcuts import render
from .models import Ingredients, Recipes
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
# Create your views here.

def index(request):

    # To fetch all the ingredients from database
    ings = Ingredients.objects.all()
    
    # Collecting User selected Ingredients in a list
    selectedIngs = request.POST.getlist('selectedIngs')

    # Code for searching Recipes by name on index page
    if 'q' in request.GET:
        q = request.GET['q']
        recs = Recipes.objects.filter (Q(Rname__icontains=q))

        # Redirect to recipe page with searched recipe
        return render(request, 'recipes.html', {'recs': recs})

    return render(request, 'index.html', {'ings' : ings})

def recipes(request):

    #To Fetch all the recipes from database
    recs = Recipes.objects.all()

    #When user submits the ingredients
    if request.method == 'POST':

        #list of user selected ingredients
        selectedIngs = request.POST.getlist('selectedIngs')
        if selectedIngs == '':
            return render(request, 'index.html')
        print(f"From recipes page{selectedIngs}")
        convertedList = [eval(i) for i in selectedIngs]
        print("Modified list is: ", convertedList)

        ###recipes = Recipes.objects.filter(Iname__in=selectedIngs)

        x = len(selectedIngs)
        print(f"Lenght of list is ={x}")
        #Converting list into integer
        for ingId in convertedList:
            print(f"this is for loop {ingId}")

                #Printing Ingredient name
            NameWithIngId = Ingredients.objects.filter(id = ingId)
            print(f"NameWithIngId= {NameWithIngId}")

                #Searching for Recipe name from ingredient id
                #This query was converted from SQL to Django
        for y in range(x):
            recipe_ids = Recipes.objects.filter(ingredientname=ingId).values().all()#.distinct()
            #print(recipe_ids)
            listToDisplay = [recipe_ids]

        return render(request, 'recipes.html', {'recs' : recipe_ids})
    
    
    # To search for recipes from recipes page
    if 'q' in request.GET:
        q = request.GET['q']
        recs = Recipes.objects.filter (Q(name__icontains=q))
    return render(request, 'recipes.html', {'recs': recs})
    
    
def singlerecipe(request):
    recipes = Recipes.objects.all()

    return render(request, 'single-recipe.html', {'recipes': recipes})

