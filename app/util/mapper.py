from fastapi import HTTPException

from app import mattermost, sentry


class WebhookMapper:
    @staticmethod
    def map_issue_alert(destination: str, request: sentry.IssueAlertWebhook) -> mattermost.IncomingWebhook:
        return mattermost.IncomingWebhook(
            channel=destination,
            attachments=mattermost.Attachment(
                title=request.data.event.title,
                fallback=request.data.event.title,
                color="#FF0000",
                author_name="Sentry",
                author_icon="https://assets.stickpng.com/images/58482eedcef1014c0b5e4a76.png",
                title_link=request.data.event.url,
                fields=[
                    mattermost.Field(
                        short=False,
                        title="Culprit",
                        value=request.data.event.culprit,
                    ),
                    mattermost.Field(
                        short=False,
                        title="Project",
                        value=request.data.event.project_slug,
                    ),
                    mattermost.Field(
                        short=False,
                        title="Project",
                        value=request.data.event.environment,
                    ),
                ],
            )
        )

    @staticmethod
    def map_metric_alert(destination: str, request: sentry.MetricAlertWebhook) -> mattermost.IncomingWebhook:
        # TODO
        raise HTTPException(status_code=501, detail="Currently Unsupported")
