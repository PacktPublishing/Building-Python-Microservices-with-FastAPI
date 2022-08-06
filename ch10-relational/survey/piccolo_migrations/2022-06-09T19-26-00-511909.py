from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2022-06-09T19:26:00:511909"
VERSION = "0.75.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="survey", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="Respondent",
        tablename="respondent",
        column_name="gender",
        db_column_name="gender",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 1,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
