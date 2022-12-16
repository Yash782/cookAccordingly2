from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recipes/', views.recipes, name='recipes'),
    path('single-recipe/', views.singlerecipe, name='single-recipe'),

]
