import datetime
from pydantic import BaseModel
from typing import Optional


class Users(BaseModel):
    u_id: Optional[int]
    u_name: str
    u_email: str
    created_at: Optional[datetime]

    # class Config:
    #     orm_mode = True


class Orders(BaseModel):
    o_id: Optional[int]
    user_id: Optional[int]
    product_name: str
    quantity: int
    order_date: datetime
