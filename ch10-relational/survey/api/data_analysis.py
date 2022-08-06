
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from survey.repository.answers import AnswerRepository
from survey.repository.location import LocationRepository

from survey.models  import weights

from sympy import Eq, symbols, Poly, solve, sympify, Ge
from sympy.parsing.sympy_parser import parse_expr

import ujson
import numpy as np
import itertools

router = APIRouter()

@router.get("/answer/respondent")
async def get_respondent_answers(qid:int):
    repo_loc = LocationRepository()
    repo_answers = AnswerRepository()
    locations = await repo_loc.get_all_location()
    data = []
    for loc in locations:
        loc_q = await repo_answers.get_answers_per_q(loc["id"], qid)
        if not len(loc_q) == 0:
            loc_data = [ weights[qid-1][str(item["answer_choice"])] for item in loc_q]
            data.append(loc_data)
    arr = np.array(data)
    return ujson.loads(ujson.dumps(arr.tolist()))
   
@router.get("/answer/increase/{gradient}")
async def answers_weight_multiply(gradient:int, qid:int):
    repo_loc = LocationRepository()
    repo_answers = AnswerRepository()
    locations = await repo_loc.get_all_location()
    data = []
    for loc in locations:
        loc_q = await repo_answers.get_answers_per_q(loc["id"], qid)
        if not len(loc_q) == 0:
            loc_data = [ weights[qid-1][str(item["answer_choice"])] for item in loc_q]
            data.append(loc_data)
    arr = np.array(list(itertools.chain(*data)))
    arr = arr * gradient
    return ujson.loads(ujson.dumps(arr.tolist()))



@router.get("/sym/inequality")
async def solve_univar_inequality(eqn:str, sol:int):
    x= symbols('x')
    
    expr1 = Ge(parse_expr(eqn, locals()), sol)
    
    sol = solve([expr1], [x])
    #sol = solve_poly_inequality( Poly(parse_expr(eqn1, locals()) ), '<')
    return str(sol)
  


@router.get("/sym/nonlinear")
async def solve_nonlinear_bivar_eqns(eqn1:str, sol1: int, eqn2:str, sol2: int):
    x, y = symbols('x, y')
      
    expr1 = parse_expr(eqn1, locals())
    expr2 = parse_expr(eqn2, locals())
    
    if not Poly(expr1, x, y).is_linear or not Poly(expr1, x, y).is_linear:
        eq1 = Eq(expr1, sol1)
        eq2 = Eq(expr2, sol2)
        sol = solve([eq1, eq2], [x, y])
        return str(sol)
    else:
        return None
  
    
@router.get("/sym/linear")
async def solve_linear_bivar_eqns(eqn1:str, sol1: int, eqn2:str, sol2: int):
    x, y = symbols('x, y')
       
    expr1 = parse_expr(eqn1, locals())
    expr2 = parse_expr(eqn2, locals())
    
    if Poly(expr1, x, y).is_linear and Poly(expr1, x, y).is_linear:
        eq1 = Eq(expr1, sol1)
        eq2 = Eq(expr2, sol2)
        sol = solve([eq1, eq2], [x, y])
        return str(sol)
    else:
        return None
    

@router.post("/sym/equation")
async def substitute_bivar_eqn(eqn: str, xval:int, yval:int):
    try:
        x, y = symbols('x, y')
        expr = sympify(eqn)
        return str(expr.subs({x: xval, y: yval}))
    except:
        return JSONResponse(content={"message": "invalid equations"}, status_code=500)
