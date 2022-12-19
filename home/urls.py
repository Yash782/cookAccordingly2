from django.contrib import admin
from django.urls import path
from django.urls import reverse
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('single-recipe/<recipe_id>', views.singlerecipe, name='single-recipe'),
    path('recipedetails/<recipe_id>', views.recipedetails, name='recipedetails'),

]
