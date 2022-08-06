import typing as t

from fastapi import FastAPI
from piccolo_admin.endpoints import create_admin
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from survey.piccolo_app import APP_CONFIG
from survey.api import login, occupation, answer, choices, location, profile, question, respondent, education, graphql, data_analysis, data_files, data_plots, data_stats

app = FastAPI(
    routes=[
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
    ],
)

app.include_router(occupation.router, prefix="/ch10")
app.include_router(login.router, prefix="/ch10")
app.include_router(answer.router, prefix="/ch10")
app.include_router(choices.router, prefix="/ch10")
app.include_router(location.router, prefix="/ch10")
app.include_router(profile.router, prefix="/ch10")
app.include_router(question.router, prefix="/ch10")
app.include_router(respondent.router, prefix="/ch10")
app.include_router(education.router, prefix="/ch10")
app.include_router(data_stats.router, prefix="/ch10")
app.include_router(data_plots.router, prefix="/ch10")
app.include_router(data_analysis.router, prefix="/ch10")
app.include_router(data_files.router, prefix="/ch10")
app.include_router(graphql.router, prefix="/ch10")

