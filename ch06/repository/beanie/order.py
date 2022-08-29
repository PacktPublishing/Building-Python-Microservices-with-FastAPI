from typing import Dict, Any
from models.data.beanie import Cart, Order

class OrderRepository: 
    
    async def insert_order(self, details:Dict[str, Any]) -> bool: 
        try:
            order = Order(**details)
            await order.insert()
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def add_order_item(self, id:int, cart_id:int): 
        try:
            item = await Cart.get(cart_id)
            order = await Order.get(id)
           
            if order.orders == None:
                order.orders = list()
                
            if not item == None:
                order.orders.append(item)    
            await order.set({Order.orders: order.orders})
            
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_order(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          cart = await Order.get(id)
          await cart.set({**details})
       except: 
           return False 
       return True
   
    async def delete_order(self, id:int) -> bool: 
        try:
            cart = await Order.get(id)
            await cart.delete()
        except: 
            return False 
        return True
    
    async def delete_order_item(self, id:int, cart_id:int): 
        try:
            order = await Order.get(id)
            item = [ i for i in order.orders if i.id == cart_id ]
            order.orders.remove(item[0])
            await order.set({Order.orders: order.orders})
        except Exception as e:
            return False 
        return True
    
    async def get_all_order(self):
        return await Order.find_all().to_list()
    
    async def get_order(self, id:int): 
        return await Order.get(id)
    
    