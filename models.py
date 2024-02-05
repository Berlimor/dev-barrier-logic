from pydantic import BaseModel


class StreamStatus(BaseModel):
    license_plate: str | None = None
    reason: str | None = None
