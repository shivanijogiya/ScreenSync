from pydantic import BaseModel
from datetime import datetime


class DeviceResponse(BaseModel):
    id: int
    device_name: str
    status: str
    last_sync: datetime

    class Config:
        from_attributes = True