from pydantic import BaseModel


class Actor(BaseModel):
    type: str | None = None
    id: str | None = None
    name: str | None = None


class Installation(BaseModel):
    uuid: str | None = None


class Webhook(BaseModel):
    action: str | None = None
    actor: Actor | None = None
    data: object | None = None
    installation: Installation | None = None