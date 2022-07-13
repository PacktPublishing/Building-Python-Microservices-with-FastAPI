from cqrs.handlers import IQueryHandler
from repository.gino.trainers import TrainerRepository
from cqrs.queries import ProfileTrainerListQuery, ProfileTrainerRecordQuery

class ListTrainerQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:TrainerRepository = TrainerRepository()
        self.query:ProfileTrainerListQuery = ProfileTrainerListQuery()
        
    async def handle(self) -> ProfileTrainerListQuery:
        data = await self.repo.get_all_member();
        self.query.records = data
        return self.query
    

class RecordTrainerQueryHandler(IQueryHandler): 
    def __init__(self): 
        self.repo:TrainerRepository = TrainerRepository()
        self.query:ProfileTrainerRecordQuery = ProfileTrainerRecordQuery()
        
    async def handle(self, id) -> ProfileTrainerListQuery:
        data = await self.repo.get_member(id);
        self.query.record = data
        return self.query