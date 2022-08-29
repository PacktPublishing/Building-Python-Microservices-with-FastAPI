from typing import Dict, Any
from models.data.beanie import Receipt, Order

class ReceiptRepository: 
    
    async def insert_receipt(self, details:Dict[str, Any]) -> bool: 
        try:
            receipt = Receipt(**details)
            await receipt.insert()
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def add_order_receipt(self, id:int, order_id:int): 
        try:
            order = await Order.get(order_id)
            receipt = await Receipt.get(id)
            await receipt.set({Receipt.order: order})
           
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def delete_order_receipt(self, id:int):
        try:
            receipt = await Receipt.get(id)
            await receipt.set({Receipt.order: None})
        except Exception as e:
            print(e)
            return False 
        return True
    
    async def update_receipt(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
          receipt = await Receipt.get(id)
          await receipt.set({**details})
       except: 
           return False 
       return True
   
    async def delete_receipt(self, id:int) -> bool: 
        try:
            receipt = await Receipt.get(id)
            await receipt.delete()
        except: 
            return False 
        return True
    
    def get_all_receipt(self):
        return Receipt.find_all().to_list()
    
    def get_receipt(self, id:int): 
        return Receipt.get(id)
    
    

