from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.schemas import DeviceResponse

from app.database import get_db
from app.models import Device

router = APIRouter(prefix="/devices", tags=["devices"])


# -----------------------------
# Register a new device
# -----------------------------
@router.post("/register")
def register_device(device_name: str, db: Session = Depends(get_db)):
    new_device = Device(
        device_name=device_name,
        status="offline",
        last_sync=datetime.utcnow()
    )

    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return {
        "status": "registered",
        "device_id": new_device.id,
        "device_name": new_device.device_name
    }


# -----------------------------
# Get all registered devices
# -----------------------------
@router.get("/", response_model=list[DeviceResponse])
def get_all_devices(db: Session = Depends(get_db)):
    devices = db.query(Device).all()

    timeout_seconds = 30   # change later if needed
    now = datetime.utcnow()

    for device in devices:
        if device.last_sync:
            if now - device.last_sync > timedelta(seconds=timeout_seconds):
                device.status = "offline"

    db.commit()

    return devices


# -----------------------------
# Device heartbeat (mark online)
# -----------------------------
@router.post("/heartbeat/{device_id}")
def heartbeat(device_id: int, db: Session = Depends(get_db)):

    device = db.query(Device).filter(Device.id == device_id).first()

    if not device:
        return {"error": "Device not found"}

    device.status = "online"
    device.last_sync = datetime.utcnow()
    db.commit()

    return {
        "message": "heartbeat received",
        "device_id": device.id,
        "status": device.status,
        "last_sync": device.last_sync
    }