"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig
from survey.tables import Answers, Education,  Question, Profile, Login, Location, Occupation, Respondent, Choices 

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="survey",
    migrations_folder_path=os.path.join(
        CURRENT_DIRECTORY, "piccolo_migrations"
    ),
    table_classes=[Answers, Education, Question, Choices, Profile, Login, Location,
                   Occupation, Respondent],
    migration_dependencies=[],
    commands=[],
)
