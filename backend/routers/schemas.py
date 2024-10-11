from pydantic import BaseModel, ConfigDict

from datetime import datetime


class PostBase(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str


class PostDisplay(BaseModel):
    id: int
    title: str
    content: str
    creator: str
    timestamp: datetime

    model_config = ConfigDict(validate=True)
