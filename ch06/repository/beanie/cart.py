from typing import Dict, Any
from models.data.beanie import Cart

class CartRepository: 
    
    async def add_item(self, details:Dict[str, Any]) -> bool: 
        try:
            receipt = Cart(**details)
            await receipt.insert()
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_qty(self, id:int, qty:int) -> bool: 
       try:
          cart = await Cart.get(id)
          await cart.set({Cart.qty:qty})
       except: 
           return False 
       return True
    
    async def add_discount(self, book_id:int, discount:float) -> bool: 
       try:
         
          cart = await Cart.find_one(Cart.book_id == book_id)
          await cart.set({Cart.discount:discount})
       except: 
           return False 
       return True
   
    async def delete_item(self, id:int) -> bool: 
        try:
            cart = await Cart.get(id)
            await cart.delete()
        except: 
            return False 
        return True
    
    async def get_cart_items(self):
        return await Cart.find_all().to_list()
    
    async def get_items_user(self, user_id:int): 
        return await Cart.find(Cart.user_id == user_id).to_list()
    
    async def get_item(self, id:int): 
        return await Cart.get(id)
    
    
    