from typing import Dict, Any
from models.data.orrs import Restaurant, Feedback, FoodRating, AmbienceRating

class RestaurantRepository: 
    
    def __init__(self, engine): 
        self.engine = engine
        
    async def insert_restaurant(self, details:Dict[str, Any]) -> bool: 
        try:
           restaurant = Restaurant(**details)
           await self.engine.save(restaurant)
                  
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_restaurant(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          restaurant = await self.engine.find_one(Restaurant, Restaurant.restaurant_id == id)
                  
          for key,value in details.items():
            setattr(restaurant,key,value)
          
          await self.engine.save(restaurant)
       except Exception as e:
           return False 
       return True
   
    async def delete_restaurant(self, id:int) -> bool: 
        try:
            restaurant = await self.engine.find_one(Restaurant, Restaurant.restaurant_id == id) 
            await self.engine.delete(restaurant)
        except: 
            return False 
        return True
    
    async def get_all_restaurant(self):
        restaurants = await self.engine.find(Restaurant)
        return restaurants
            
    async def get_restaurant(self, id:int): 
        restaurant = await self.engine.find_one(Restaurant, Restaurant.restaurant_id == id) 
        return restaurant
    
    async def add_feedback(self, id:int, details:Dict[str, Any]):
       try:
          restaurant = await self.engine.find_one(Restaurant, Restaurant.restaurant_id == id)
          feedback = Feedback(**details)        
          restaurant.feedback.append(feedback)         
          await self.engine.save(restaurant)
       except Exception as e:
           return False 
       return True 
    
    async def add_food_rating(self, id:int, details:Dict[str, Any]):
       try:
          restaurant = await self.engine.find_one(Restaurant, Restaurant.restaurant_id == id)
                  
          food_rate = FoodRating(**details)
          restaurant.food_rating.append(food_rate)
          
          await self.engine.save(restaurant)
       except Exception as e:
           return False 
       return True 
    
    async def add_ambience_rating(self, id:int, details:Dict[str, Any]): 
       try:
          restaurant = await self.engine.find_one(Restaurant, Restaurant.restaurant_id == id)
                  
          ambiance_rate = AmbienceRating(**details)
          restaurant.ambiance_rating.append(ambiance_rate)
          await self.engine.save(restaurant)
       except Exception as e:
           print(e)
           return False 
       return True