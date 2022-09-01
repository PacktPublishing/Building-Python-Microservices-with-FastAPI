from models.data.nsms import Billing, Admin, Vendor
from datetime import date, time
from typing import List, Dict, Any

class BillingRepository: 
    
    async def insert_billing(self, details:Dict[str, Any]) -> bool: 
        try:
            await Billing.create(**details)
        except Exception as e: 
            print(e)
            return False 
        return True
    
    async def update_billing(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
         billing = await Billing.get(id)
         # await Billing.update.values(**details).where(Billing.id == id).gino.status()
         await billing.update(**details).apply()
       except: 
           return False 
       return True
   
    async def delete_billing(self, id:int) -> bool: 
        try:
            admin = await Billing.get(id)
            await admin.delete()
            # await Billing.delete.where(Billing.id == id).gino.status()
        except Exception as e: 
            return False 
        return True
    
    async def get_all_billing(self):
        return await Billing.query.gino.all()
        
    async def get_billing(self, id:int): 
        return await Billing.get(id)
    
class BillingAdminRepository:
        
    async def join_billing_admin(self):
        query = Billing.join(Admin).select()
        result = await query.gino.load(Billing.distinct(Billing.id).load(parent=Admin)).all()
        return result 
    
    async def join_admin_billing(self):

        result = await Admin.load(add_child=Billing).query.gino.all()
        return result   

class BillingVendorRepository:
    
    async def join_billing_vendor(self):
        query = Billing.join(Vendor).select()
        result = await query.gino.load(Billing.distinct(Billing.id).load(parent=Vendor)).all()
        return result 
    
    async def join_vendor_billing(self):
        result = await Vendor.load(add_child=Billing).query.gino.all()
        return result 
    