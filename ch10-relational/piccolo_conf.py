from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry


DB = PostgresEngine(
    config={
        "database": "pccs",
        "user": "postgres",
        "password": "admin2255",
        "host": "localhost",
        "port": 5433,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["survey.piccolo_app", "piccolo_admin.piccolo_app"]
)
