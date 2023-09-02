from typing import List

from pydantic import BaseModel

from app import sentry


class Trigger(BaseModel):
    actions: List[object] | None = None


class AlertRule(BaseModel):
    triggers: List[Trigger] | None = None


class MetricAlert(BaseModel):
    alert_rule: AlertRule | None = None


class Data(BaseModel):
    description_text: str
    description_title: str
    metric_alert: MetricAlert
    web_url: str


class MetricAlertWebhook(sentry.Webhook):
    """
    source: https://docs.sentry.io/product/integrations/integration-platform/webhooks/metric-alerts/
    """
    data: Data | None = None
