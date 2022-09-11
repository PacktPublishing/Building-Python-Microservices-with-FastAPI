from  fastapi import FastAPI

from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler, make_playground_handler
from config.pccs import db_connect, db_close

from api import survey_graphene_login, survey_graphene_profile, survey_neo4j, survey_workflow

app = FastAPI()
app.include_router(survey_neo4j.router, prefix="/ch10")
app.include_router(survey_workflow.router, prefix="/ch10")
app.mount("/ch10/graphql/login", GraphQLApp(survey_graphene_login.schema, on_get=make_playground_handler()) )
app.mount("/ch10/graphql/profile", GraphQLApp(survey_graphene_profile.schema, on_get=make_playground_handler()) )

@app.on_event("startup")
async def initialize():
    await db_connect()

@app.on_event("shutdown")
async def destroy():
    await db_close()

