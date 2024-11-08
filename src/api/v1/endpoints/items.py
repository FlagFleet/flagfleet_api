from dependency_injector.wiring import Provide, inject
from fastapi import Depends, APIRouter
from pydantic import Field
from sqlmodel import Session, select
from ....dependencies import Container
from ....models.base import TimestampModel
from typing import List, Optional

router = APIRouter()

class Item(TimestampModel, table=True):
    id: Optional[int] = Field(default=None)
    name: str
    description: str = Field(default=None)

@router.get("/items/", response_model=List[Item])
@inject
async def get_items(
    session: Session = Depends(Provide[Container.db_session])
):
    items = session.exec(select(Item)).all()
    return items
