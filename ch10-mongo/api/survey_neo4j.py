from fastapi import APIRouter 
from fastapi.responses import JSONResponse

from config.pcss_neo4j import driver
from models.request.pccs_neo4j import LocationReq, ProfileReq, RespondentReq, LinkAdminLoc, LinkAdminRespondent, LinkRespondentLoc


router = APIRouter()

               
@router.post("/neo4j/location/add")
def create_survey_loc(node_name: str, node_req_atts: LocationReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
    query = f"CREATE ({node_name}:Location  {node_attributes})"
    try:
        with driver.session() as session:
            session.run(query=query)
                       
        return JSONResponse(content={"message": "add node location successful"}, status_code=201)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "add node location unsuccessful"}, status_code=500)

@router.post("/neo4j/surveyor/add")
def create_survey_admin(node_name: str, node_req_atts: ProfileReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
   
    query = f"CREATE ({node_name}:Administrator  {node_attributes})"
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "add node administrator successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "add node administrator unsuccessful"}, status_code=500)

@router.post("/neo4j/respondent/add")
def create_survey_respondent(node_name: str, node_req_atts: RespondentReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
   
    query = f"CREATE ({node_name}:Respondent  {node_attributes})"
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "add node respondent successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "add node respondent unsuccessful"}, status_code=500)


@router.post("/neo4j/link/admin/loc")
def link_admin_loc(admin_node: str, loc_node: str, node_req_atts:LinkAdminLoc):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
  
    query = f"""
        MATCH (admin:Administrator), (loc:Location)
        WHERE admin.name = '{admin_node}' AND loc.name = '{loc_node}'
        CREATE (admin) -[relationship:ASSIGNED_TO {node_attributes}]->(loc)"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "add administrator-loc relationship successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "add administrator-loc relationship unsuccessful"}, status_code=500)

@router.post("/neo4j/link/respondent/loc")
def link_respondent_loc(respondent_node: str, loc_node: str, node_req_atts:LinkRespondentLoc):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
   
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
  
    query = f"""
        MATCH (respondent:Respondent), (loc:Location)
        WHERE respondent.name = '{respondent_node}' AND loc.name = '{loc_node}'
        CREATE (respondent) -[relationship:LIVES_IN {node_attributes}]->(loc)"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "add respondent-loc relationship successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "add respondent-loc relationship unsuccessful"}, status_code=500)

@router.post("/neo4j/link/administrator/respondent")
def link_respondent_admin(respondent_node: str, administrator: str, node_req_atts:LinkAdminRespondent):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
   
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
  
    query = f"""
        MATCH (respondent:Respondent), (administrator:Administrator)
        WHERE respondent.name = '{respondent_node}' AND administrator.name = '{administrator}'
        CREATE (administrator) -[relationship:CONDUCTED_SURVEY_TO {node_attributes}]->(respondent)"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "add respondent-loc relationship successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "add respondent-loc relationship unsuccessful"}, status_code=500)

@router.patch("/neo4j/update/location/{id}")
async def update_node_loc(id:int, node_req_atts: LocationReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
    query = f"""
        MATCH (location:Location)
        WHERE ID(location) = {id}
        SET location += {node_attributes}"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "update location successful"}, status_code=201)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "update location  unsuccessful"}, status_code=500)

@router.patch("/neo4j/update/administrator/{id}")
async def update_node_admin(id:int, node_req_atts: ProfileReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
    query = f"""
        MATCH (admin:Administrator)
        WHERE ID(admin) = {id}
        SET admin += {node_attributes}"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "update administrator node successful"}, status_code=201)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "update administrator node unsuccessful"}, status_code=500)

@router.get("/neo4j/nodes/all")
async def list_all_nodes():
    query = f"""
        MATCH (node)
        RETURN node"""
    try:
        with driver.session() as session:
            result = session.run(query=query)
            nodes = result.data()
        return nodes
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "listing all nodes unsuccessful"}, status_code=500)
    
@router.get("/neo4j/location/{id}")
async def get_location(id:int):
    query = f"""
        MATCH (node:Location)
        WHERE ID(node) = {id}
        RETURN node"""
    try:
        with driver.session() as session:
            result = session.run(query=query)
            nodes = result.data()
        return nodes
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "get location node unsuccessful"}, status_code=500)
    
@router.get("/neo4j/administrator/{id}")
async def get_administrator(id:int):
    query = f"""
        MATCH (node:Administrator)
        WHERE ID(node) = {id}
        RETURN node"""
    try:
        with driver.session() as session:
            result = session.run(query=query)
            nodes = result.data()
        return nodes
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "get location node unsuccessful"}, status_code=500)

@router.get("/neo4j/respondent/{id}")
async def get_respondent(id:int):
    query = f"""
        MATCH (node:Respondent)
        WHERE ID(node) = {id}
        RETURN node"""
    try:
        with driver.session() as session:
            result = session.run(query=query)
            nodes = result.data()
        return nodes
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "get respondent node unsuccessful"}, status_code=500)

@router.patch("/neo4j/update/respondent/{id}")
async def update_node_respondent(id:int, node_req_atts: RespondentReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
    query = f"""
        MATCH (respondent:Respondent)
        WHERE ID(respondent) = {id}
        SET respondent += {node_attributes}"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "update respondent node successful"}, status_code=201)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "update respondent node unsuccessful"}, status_code=500)

@router.patch("/neo4j/update/location/{id}")
async def update_node_location(id:int, node_req_atts: LocationReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
    query = f"""
        MATCH (location:Location)
        WHERE ID(location) = {id}
        SET location += {node_attributes}"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "update location node successful"}, status_code=201)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "update location node unsuccessful"}, status_code=500)

@router.patch("/neo4j/update/administrator/{id}")
async def update_node_administrator(id:int, node_req_atts: ProfileReq):
    node_attributes_dict = node_req_atts.dict(exclude_unset=True)
    node_attributes = '{' + ', '.join(f'{key}:\'{value}\'' for (key, value) in node_attributes_dict.items()) + '}'
    query = f"""
        MATCH (administrator:Administrator)
        WHERE ID(administrator) = {id}
        SET administrator += {node_attributes}"""
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "update administrator node successful"}, status_code=201)
    except Exception as e:
        print(e)
        return JSONResponse(content={"message": "update administrator node unsuccessful"}, status_code=500)


@router.delete("/neo4j/delete/admin/{node}")
def delete_admin_node(node:str):
    node_attributes = '{' + f"name:'{node}'" + '}'
    
    query = f"""
        MATCH (n:Administrator {node_attributes})
        DETACH DELETE n
    """
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "delete admin node successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "delete admin node unsuccessful"}, status_code=500)


@router.delete("/neo4j/delete/location/{node}")
def delete_location_node(node:str):
    node_attributes = '{' + f"name:'{node}'" + '}'
    query = f"""
        MATCH (n:Location {node_attributes})
        DETACH DELETE n
    """
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "delete location node successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "delete location node unsuccessful"}, status_code=500)

@router.delete("/neo4j/delete/respondent/{node}")
def delete_respondent_node(node:str):
    node_attributes = '{' + f"name:'{node}'" + '}'
    query = f"""
        MATCH (n:Respondent {node_attributes})
        DETACH DELETE n
    """
    try:
        with driver.session() as session:
            session.run(query=query)
        return JSONResponse(content={"message": "delete respondent node successful"}, status_code=201)
    except:
        return JSONResponse(content={"message": "delete respondent node unsuccessful"}, status_code=500)