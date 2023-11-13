from fastapi import APIRouter, Depends
from typing import Optional
from services import weather_api_service, weather_report_service
from model import ReportSubmittal

router = APIRouter()


@router.get("/api/weather/reports", name="all reports", status_code=200)
def get_weather_report():
    return weather_report_service.get_all_weather_report()


@router.get("/api/weather/{city}")
async def weather_info(
    city: str,
    state: str,
    country: Optional[str] = "US",
    units: Optional[str] = "Metric",
):
    # return {"weather": f"{city}, {state}, {country},{units}"}
    # return weather_api_service.get_weather_data(
    #     city=city, state=state, country=country
    # )
    return await weather_api_service.get_weather_data_async(
        city=city, state=state, country=country
    )


@router.post("/api/weather/report", name="add weather report", status_code=201)
def add_weather_report(report: ReportSubmittal):
    return weather_report_service.add_weather_report_db(
        description=report.description, location=report.location
    )
