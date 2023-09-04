from fastapi import HTTPException

from app import mattermost, sentry


class WebhookMapper:
    @staticmethod
    def map_issue_alert(
            request: sentry.IssueAlertWebhook,
            icon_path: str = "https://assets.stickpng.com/images/58482eedcef1014c0b5e4a76.png"
    ) -> mattermost.IncomingWebhook:
        return mattermost.IncomingWebhook(
            username="Sentry",
            attachments=[
                mattermost.Attachment(
                    text=request.data.event.title + "@" + request.data.event.culprit,
                    title=request.data.event.title,
                    fallback="Error reported by Sentry: " + request.data.event.title,
                    color="#FF0000",
                    author_name="Sentry",
                    author_icon=icon_path,
                    author_link="test_link",
                    title_link=request.data.event.issue_url,
                    fields=[
                        mattermost.Field(
                            short=True,
                            title="Culprit",
                            value=request.data.event.culprit,
                        ),
                        mattermost.Field(
                            short=True,
                            title="Platform",
                            value=request.data.event.platform,
                        ),
                        mattermost.Field(
                            short=True,
                            title="Event",
                            value=request.data.event.url,
                        ),
                        mattermost.Field(
                            short=True,
                            title="Environment",
                            value=request.data.event.environment,
                        ),
                        mattermost.Field(
                            short=True,
                            title="Function",
                            value=request.data.event.metadata.function,
                        ),
                        mattermost.Field(
                            short=True,
                            title="File",
                            value=request.data.event.metadata.filename,
                        ),
                    ],
                ),
            ]
        )

    @staticmethod
    def map_metric_alert(destination: str, request: sentry.MetricAlertWebhook) -> mattermost.IncomingWebhook:
        # TODO
        raise HTTPException(status_code=501, detail="Currently Unsupported")
