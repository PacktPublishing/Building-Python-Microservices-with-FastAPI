from enum import Enum

class Category(str, Enum):
    breakfast = "breakfast"
    lunch = "lunch"
    dinner = "dinner"
    appetizer = "appetizer"
    salad = "salad"
    entree = "entree"
    side_dish = "side_dish"
    pastry = "pastry"
    dessert = "dessert"
    snack = "snack"
    soup = "soup"
    holiday = "holiday"
    vegetarian = "vegetarian"
    cookbook = "cookbook"

class Origin(str, Enum):
    asian = "asian"
    mediterranean = "mediterranean"
    mid_eastern = "mid_eastern"
    african = "african"
    pacific = "pacific"
    south_american = "south_american"
    north_american = "south_american"
    european = "european"
    jewish = "jewish"
    carribean = "carribean"
    
class UserType(str, Enum): 
    admin = "admin"
    user = "user"
    guest = "guest"

class RecipeRating(str, Enum):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"