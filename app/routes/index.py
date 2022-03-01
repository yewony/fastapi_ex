from datetime import datetime
from re import A
from anyio import current_time as frame
# from inspect import current_time as frame

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.requests import Request

from app.database.conn import db
from app.database.schema import Users

router = APIRouter()

@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    ELB 상태 체크용 API
    :return:
    """
    Users().get(session, email="edreghorn4@ucla.edu")
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
