from typing import List

from pydantic import BaseModel


class Field(BaseModel):
    title: str | None = None
    value: str | None = None
    short: bool | None = None


class Attachment(BaseModel):
    """
    source: https://developers.mattermost.com/integrate/reference/message-attachments/
    """
    fallback: str | None = None
    color: str | None = None
    pretext: str | None = None
    text: str | None = None
    author_name: str | None = None
    author_link: str | None = None
    author_icon: str | None = None
    title: str | None = None
    title_link: str | None = None
    fields: List[Field] | None = None
    image_url: str | None = None
    thumb_url: str | None = None
    footer: str | None = None
    footer_icon: str | None = None


class IncomingWebhook(BaseModel):
    """
    source: https://developers.mattermost.com/integrate/webhooks/incoming/
    """
    text: str | None = None
    channel: str | None = None
    username: str | None = None
    icon_url: str | None = None
    icon_emoji: str | None = None
    attachments: Attachment | None = None
    type: str | None = None
    props: object | None = None
