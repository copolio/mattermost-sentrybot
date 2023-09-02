from unittest import TestCase

from app.sentry.metric_alert import MetricAlertWebhook


class TestMetricAlertWebhook(TestCase):
    def test_request_deserialize_success(self):
        # given
        json_dict = {
            "action": "resolved",
            "actor": {
                "id": "sentry",
                "name": "Sentry",
                "type": "application"
            },
            "data": {
                "description_text": "1000 events in the last 10 minutes\\nFilter: level:error",
                "description_title": "Resolved: Too many errors",
                "metric_alert": {
                    "alert_rule": {
                        "aggregate": "count()",
                        "created_by": None,
                        "dataset": "events",
                        "date_created": "2020-09-13T12:26:40.000000Z",
                        "date_modified": "2020-09-13T12:26:40.000000Z",
                        "environment": None,
                        "id": "7",
                        "include_all_projects": False,
                        "name": "Too many errors",
                        "organization_id": "5",
                        "projects": ["bar"],
                        "query": "level:error",
                        "resolution": 1,
                        "resolve_threshold": None,
                        "status": 0,
                        "threshold_period": 1,
                        "threshold_type": 0,
                        "time_window": 10,
                        "triggers": []
                    },
                    "date_closed": None,
                    "date_created": "2020-09-13T12:26:40.000000Z",
                    "date_detected": "2020-09-13T12:26:40.000000Z",
                    "date_started": "2020-09-13T12:26:40.000000Z",
                    "id": "4",
                    "identifier": "1",
                    "organization_id": "5",
                    "projects": ["bar"],
                    "status": 2,
                    "status_method": 3,
                    "title": "Sacred Marmot",
                    "type": 2
                },
                "web_url": "https://sentry.io/organizations/baz/alerts/1/"
            },
            "installation": {
                "uuid": "a8e5d37a-696c-4c54-adb5-b3f28d64c7de"
            }
        }
        # when
        metric_alert_webhook = MetricAlertWebhook.model_validate(json_dict)
        # then
        self.assertEquals("resolved", metric_alert_webhook.action)

    pass
