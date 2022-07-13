
from uuid import UUID
from model.classifications import Category, Origin
from typing import List

class Ingredient:
    def __init__(self, id: UUID, name:str, qty : float, measure : str):
        self.id = id
        self.name = name
        self.qty = qty
        self.measure = measure
        
        
class Recipe:
    def __init__(self, id: UUID, name:str, ingredients: List[Ingredient], cat: Category, orig : Origin):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.cat = cat
        self.orig = orig