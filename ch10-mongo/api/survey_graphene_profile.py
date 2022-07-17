from models.data.pccs_graphql import ProfileData
from graphene import ObjectType, List, String, Schema, Field, Mutation, Boolean, Int, Date
from repository.profile import ProfileRepository

from datetime import date, datetime
from json import dumps, loads
import os

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    raise TypeError ("The type %s not serializable." % type(obj))
  
class ProfileQuery(ObjectType):
    profile_list = None
    get_profile = Field(List(ProfileData))
  
    async def resolve_get_profile(self, info):
      repo = ProfileRepository()
      profile_list = await repo.get_all_profile()
      print(profile_list)
      return profile_list

class CreateProfileData(Mutation):
    class Arguments:
      id = Int(required=True)
      fname = String(required=True)
      lname = String(required=True)
      age = Int(required=True)
      position = String(required=True)
      login_id = Int(required=True)
      official_id = String(required=True)
      date_employed = Date()
      

    ok = Boolean()
    profileData = Field(lambda: ProfileData)

    async def mutate(root, info, id, fname, lname, age, position, login_id, official_id, date_employed):
        
        profile_dict = {"id": id, "fname": fname, "lname": lname, "age": age, "position": position,
                      "login_id": login_id, "official_id": official_id, "date_employed": date_employed}
        profile_json = dumps(profile_dict, default=json_serial)
        repo = ProfileRepository()
        result = await repo.add_profile(loads(profile_json))
        if not result == None:
          ok = True
        else: 
          ok = False
        return CreateProfileData(profileData=result, ok=ok)


class PorfileMutations(ObjectType):
    create_profile = CreateProfileData.Field()
   
      
schema = Schema(query=ProfileQuery, mutation=PorfileMutations,
    auto_camelcase=False,)