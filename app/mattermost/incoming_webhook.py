from typing import List

from pydantic import BaseModel


class Field(BaseModel):
    title: str
    value: str
    short: bool


class Attachment(BaseModel):
    """
    source: https://developers.mattermost.com/integrate/reference/message-attachments/
    """
    fallback: str
    color: str
    pretext: str
    text: str
    author_name: str
    author_link: str
    author_icon: str
    title: str
    title_link: str
    fields: List[Field]
    image_url: str
    thumb_url: str
    footer: str
    footer_icon: str


class IncomingWebhook(BaseModel):
    """
    source: https://developers.mattermost.com/integrate/webhooks/incoming/
    """
    text: str
    channel: str
    username: str
    icon_url: str
    icon_emoji: str
    attachments: Attachment
    type: str
    props: object
