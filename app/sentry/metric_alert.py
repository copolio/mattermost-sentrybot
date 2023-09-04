from typing import List

from pydantic import BaseModel

from app import sentry


class Trigger(BaseModel):
    actions: List[object] | None = None


class AlertRule(BaseModel):
    triggers: List[Trigger] | None = None
    name: str | None = None
    projects: List[str] | None = None


class MetricAlert(BaseModel):
    alert_rule: AlertRule | None = None


class Data(BaseModel):
    description_text: str | None = None
    description_title: str | None = None
    metric_alert: MetricAlert | None = None
    web_url: str | None = None


class MetricAlertWebhook(sentry.Webhook):
    """
    source: https://docs.sentry.io/product/integrations/integration-platform/webhooks/metric-alerts/
    """
    data: Data | None = None
