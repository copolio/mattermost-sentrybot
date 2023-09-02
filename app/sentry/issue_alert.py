from pydantic import BaseModel

from app import sentry


class Event(BaseModel):
    url: str | None = None
    web_url: str | None = None
    issue_url: str | None = None
    issue_id: str | None = None


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
