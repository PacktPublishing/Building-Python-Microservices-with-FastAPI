from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from faculty_mgt.models.request.assignment import AssignmentRequest
from faculty_mgt.models.data.faculty import Assignment
from faculty_mgt.services.assignments import AssignmentSubmissionService, AssignmentService

from datetime import datetime

router = APIRouter()

@router.get("/assignments/list")
async def provide_assignments(): 
    assignment_service:AssignmentService = AssignmentService()
    return assignment_service.list_assignment()

@router.post("/assignments/faculty")
def create_assignment(assignment:AssignmentRequest): 
    item = Assignment(title=assignment.title,date_due=assignment.date_due, course=assignment.course, assgn_id=assignment.assgn_id)
    assignment_service:AssignmentService = AssignmentService()
    result = assignment_service.add_assignment(item)
    if result == True: 
        return jsonable_encoder(item)
    else: 
        return JSONResponse(content={'message':'create assignment problem encountered'}, status_code=500)

@router.post('/assignments/student/submit')
def submit_assignment(assignment:AssignmentRequest): 
    item = Assignment(title=assignment.title,date_due=assignment.date_due, course=assignment.course, assgn_id=assignment.assgn_id)
    item.date_completed = datetime.now()
    assignment_submission_service:AssignmentSubmissionService = AssignmentSubmissionService()
    result = assignment_submission_service.add_assigment(assignment.bin_id, item)
    if result == True: 
        return jsonable_encoder(item)
    else: 
        return JSONResponse(content={'message':'submission problem encountered'}, status_code=500)

@router.post('/assignments/student/workbin')
def create_workbin(stud_id:int, faculty_id:int): 
    assignment_submission_service:AssignmentSubmissionService = AssignmentSubmissionService()
    result, bin_id = assignment_submission_service.create_workbin(stud_id, faculty_id)
    if result == True: 
        return JSONResponse(content={'message':'workbin %s is created successful'%(bin_id)}, status_code=201)
    else: 
        return JSONResponse(content={'message':'submission problem encountered'}, status_code=500)

@router.post('/assignments/view/workbins')
def view_workbins(bin_id:int): 
    assignment_submission_service:AssignmentSubmissionService = AssignmentSubmissionService()
    return  assignment_submission_service.list_assignments(bin_id)


