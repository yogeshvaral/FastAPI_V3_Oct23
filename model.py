from pydantic import BaseModel
import datetime
from typing import Optional, List

order_jason = {
    "item_id": "123",
    "created_date": "2023-11-14 12:22",
    "pages_visited": [1, 2, "3"],
    "prices": 17.22,
}


class Order(BaseModel):
    item_id: int
    created_date: Optional[datetime.datetime]
    pages_visited: List[int]
    prices: float


o = Order(**order_jason)
print(o)


class Location(BaseModel):
    city: str
    state: Optional[str]
    country: Optional[str]


class ReportSubmittal(BaseModel):
    description: str
    location: Location


class Report(ReportSubmittal):
    uuid: str
    date: Optional[datetime.datetime]
