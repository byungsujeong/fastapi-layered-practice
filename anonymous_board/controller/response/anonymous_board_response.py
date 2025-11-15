from datetime import datetime

from pydantic import BaseModel, ConfigDict, field_serializer


class AnonymousBoardResponse(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime, _info):
        return value.isoformat()
    