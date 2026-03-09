from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String, index=True)
    status = Column(String, default="offline")
    last_sync = Column(DateTime, default=datetime.utcnow)