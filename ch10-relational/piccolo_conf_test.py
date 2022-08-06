from piccolo_conf import *  # noqa


DB = PostgresEngine(
    config={
        "database": "piccolo_project_test",
        "user": "postgres",
        "password": "",
        "host": "localhost",
        "port": 5432,
    }
)
