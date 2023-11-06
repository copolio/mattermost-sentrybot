from enum import Enum

from pydantic import BaseModel


class SentryHookResource(str, Enum):
    EVENT = "event_alert",
    METRIC = "metric_alert"
    INSTALLATION = "installation"
    ISSUE = "issue"
    ERROR = "error"
    COMMENT = "comment"


class Actor(BaseModel):
    type: str | None = None
    id: str | int | None = None
    name: str | None = None


class Installation(BaseModel):
    uuid: str | None = None


class Webhook(BaseModel):
    action: str | None = None
    actor: Actor | None = None
    data: dict | object | None = None
    installation: Installation | None = None
