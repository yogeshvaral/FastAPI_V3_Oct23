from fastapi import APIRouter, Response
from typing import Optional

router = APIRouter()


@router.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return Response(
            content='{"error":"ERROR :Z can not be zero"}',
            media_type="application/json",
            status_code=400,
        )
    value = x + y
    if z is not None:
        value = value / z
    return {"value": value}
