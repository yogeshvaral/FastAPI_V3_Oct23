from typing import List
from fastapi import Depends
from model import Report, ReportSubmittal, Location
import datetime
import uuid
import json


__report: List[Report] = []


def get_all_weather_report() -> List[Report]:
    return list(__report)


def add_weather_report_db(description: str, location: Location):
    now = datetime.datetime.now()
    report = Report(
        description=description, location=location, date=now, uuid=str(uuid.uuid4())
    )
    __report.append(report)
    return report
