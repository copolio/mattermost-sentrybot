from pydantic import BaseModel

from app import sentry


class MetaData(BaseModel):
    filename: str | None = None
    type: str | None = None
    value: str | None = None
    function: str | None = None


class Event(BaseModel):
    title: str | None = None
    url: str | None = None
    web_url: str | None = None
    issue_url: str | None = None
    issue_id: str | None = None
    culprit: str | None = None
    environment: str | None = None
    project_slug: str | None = None
    project: int | None = None
    platform: str | None = None
    metadata: MetaData | None = None


class IssueAlert(BaseModel):
    title: str | None = None
    settings: object | None = None


class Data(BaseModel):
    event: Event | None = None
    issue_alert: IssueAlert | None = None
    triggered_rule: str | None = None


class IssueAlertWebhook(sentry.Webhook):
    """
    source: https://docs.sentry.io/product/integrations/integration-platform/webhooks/issue-alerts/
    """
    data: Data | None = None
