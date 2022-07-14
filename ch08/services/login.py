import asyncio
from models.data.nsms import Login


@asyncio.coroutine
def build_user_list(query_list):
    user_list = []
    for record in query_list:
        yield from asyncio.sleep(2)
        user_list.append(" ".join([str(record.id), record.username, record.password]))
    return user_list
        
        

async def count_login(query_list):
    await asyncio.sleep(2)
    return len(query_list)


