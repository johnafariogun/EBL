from fastapi import APIRouter

router = APIRouter(prefix='/ebl', tags=['EBL'])

@router.get('/')
async def hello():
    return {"message":"this is john, learning a new technology"}
