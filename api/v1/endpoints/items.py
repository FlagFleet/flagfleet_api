from dependency_injector.wiring import Provide, inject
from fastapi import Depends, APIRouter
from sqlmodel import Session, select, Field
from typing import List, Optional

from dependencies import Container
from models.base import TimestampModel

router = APIRouter()

class Item(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str = Field(default=None)

@router.get("/items/", response_model=List[Item])
@inject
async def get_items(
    session: Session = Depends(Provide[Container.db_session])
):
    print(session)
    items = session.exec(select(Item)).all()
    return items
