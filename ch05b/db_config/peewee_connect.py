from peewee import PostgresqlDatabase, _ConnectionState
from contextvars import ContextVar

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(_ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

db = PostgresqlDatabase(
    'fcms2',
    user='postgres',
    password='admin2255',
    host='localhost',
    port=5433, 
)

db._state = PeeweeConnectionState()