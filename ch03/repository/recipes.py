from model.recipes import Recipe
from model.recipes import Ingredient
from model.classifications import Category, Origin
from uuid import uuid1 

recipes = dict()

class RecipeRepository: 
    def __init__(self): 
        ingrA1 = Ingredient(measure='cup', qty=1, name='grape tomatoes', id=uuid1())
        ingrA2 = Ingredient(measure='teaspoon', qty=0.5, name='salt', id=uuid1())
        ingrA3 = Ingredient(measure='pepper', qty=0.25, name='pepper', id=uuid1())
        ingrA4 = Ingredient(measure='pound', qty=0.5, name='asparagus', id=uuid1())
        ingrA5 = Ingredient(measure='teaspoon', qty=2, name='olive oil', id=uuid1())
        ingrA6 = Ingredient(measure='pieces', qty=4, name='large eggs', id=uuid1())
        ingrA7 = Ingredient(measure='cup', qty=1, name='milk', id=uuid1())
        ingrA8 = Ingredient(measure='cup', qty=0.5, name='whipped cream cheese', id=uuid1())
        ingrA9 = Ingredient(measure='cup', qty=0.25, name='Parmesan cheese', id=uuid1())
    
        recipeA = Recipe(orig=Origin.european ,ingredients= [ingrA1, ingrA2, ingrA3, ingrA4, ingrA5, ingrA6, ingrA7, ingrA8, ingrA9], cat= Category.breakfast, name='Crustless quiche bites with asparagus and oven-dried tomatoes', id=uuid1())

        ingrB1 = Ingredient(measure='tablespoon', qty=1, name='oil', id=uuid1())
        ingrB2 = Ingredient(measure='cup', qty=0.5, name='chopped tomatoes', id=uuid1())
        ingrB3 = Ingredient(measure='minced', qty=1, name='pepper', id=uuid1())
        ingrB4 = Ingredient(measure='drop', qty=1, name='salt', id=uuid1())
        ingrB5 = Ingredient(measure='pieces', qty=2, name='large eggs', id=uuid1())
    
        recipeB = Recipe(orig=Origin.carribean ,ingredients= [ingrB1, ingrB2, ingrB3, ingrB4, ingrB5], cat= Category.breakfast, name='Fried eggs, Caribbean style', id=uuid1())

        ingrC1 = Ingredient(measure='pounds', qty=2.25, name='sweet yellow onions', id=uuid1())
        ingrC2 = Ingredient(measure='cloves', qty=10, name='garlic', id=uuid1())
        ingrC3 = Ingredient(measure='minced', qty=1, name='blackpepper', id=uuid1())
        ingrC4 = Ingredient(measure='drop', qty=1, name='kasher salt', id=uuid1())
        ingrC5 = Ingredient(measure='cup', qty=4, name='low-sodium chicken brothlarge eggs', id=uuid1())
        ingrC6 = Ingredient(measure='tablespoon', qty=4, name='sherry', id=uuid1())
        ingrC7 = Ingredient(measure='sprig', qty=7, name='thyme', id=uuid1())
        ingrC8 = Ingredient(measure='cup', qty=0.5, name='heavy cream', id=uuid1())
        
        recipeC = Recipe(orig=Origin.mediterranean ,ingredients= [ingrC1, ingrC2, ingrC3, ingrC4, ingrC5, ingrC6, ingrC7, ingrC8], cat= Category.soup, name='Creamy roasted onion soup', id=uuid1())
        
        recipes[recipeA.id] = recipeA
        recipes[recipeB.id] = recipeB
        recipes[recipeC.id] = recipeC
        
    def insert_recipe(self, recipe: Recipe):
        recipes[recipe.id] = recipe
        
    def query_recipes(self):
        return recipes

