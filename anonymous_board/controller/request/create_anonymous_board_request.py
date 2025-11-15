from datetime import datetime

from pydantic import BaseModel


class CreateAnonymousBoardRequest(BaseModel):
    title: str
    content: str