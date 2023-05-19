from enum import Enum, unique
from pydantic import BaseModel


@unique
class AlertType(Enum):
    email    = 'email'
    dingding = 'dingding'
    telegram = 'telegram'


class SendType(BaseModel):
    type: AlertType
