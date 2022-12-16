from django.db import models

# Create your models here.

class Ingredients(models.Model):
    Iname = models.CharField(max_length=50)
    Itypes = (
        ('Dairy', 'Dairy'),
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Speces', 'Speces'),
        ('Nuts and Oil', 'Nuts and Oil Seeds'),
        ('Lentils', 'Lentils'),
        ('Cereals', 'Cereals'),
        ('Flours', 'Flours'),
        ('Grains', 'Grains'),
        ('Meat', 'Meat'),
        ('Pantry', 'Pantry'),
    )
    Itype = models.CharField(max_length=50, choices=Itypes)
    def __str__(self):
        return self.Iname

class Recipes(models.Model):
    Rname = models.CharField(max_length=100)
    Rimg = models.ImageField(null=True, blank= True, upload_to='photos')
    Rdesc = models.TextField()
    Iname = models.ManyToManyField(Ingredients)
    Rtypes = (
        ('Breakfast', 'Breakfast'),
        ('Meals', 'Meals')
    )
    Rtype = models.CharField(max_length=20, choices=Rtypes)
    def __str__(self):
        return self.Rname

class Nutritionalvals(models.Model):
    
    Rname = models.OneToOneField(Recipes, on_delete=models.CASCADE)
    calories = models.CharField(max_length=10)
    fats = models.CharField(max_length=10)
    protien = models.CharField(max_length=10)
    carbs = models.CharField(max_length=10)
    NRname = models.CharField(max_length=50)

    def __str__(self):
        return self.NRname

