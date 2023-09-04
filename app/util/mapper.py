from app import mattermost, sentry


class WebhookMapper:
    @staticmethod
    def map_issue_alert(
            request: sentry.IssueAlertWebhook,
            icon_path: str = "https://assets.stickpng.com/images/58482eedcef1014c0b5e4a76.png"
    ) -> mattermost.IncomingWebhook:
        return mattermost.IncomingWebhook(
            username=request.actor.name,
            attachments=[
                mattermost.Attachment(
                    text=request.data.event.title + "@" + request.data.event.culprit,
                    title=request.data.event.title,
                    fallback="Issue Alert reported by Sentry: " + request.actor.name,
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
                )
            ]
        )

    @staticmethod
    def map_metric_alert(
            request: sentry.MetricAlertWebhook,
            icon_path: str = "https://assets.stickpng.com/images/58482eedcef1014c0b5e4a76.png"
    ) -> mattermost.IncomingWebhook:
        return mattermost.IncomingWebhook(
            username=request.actor.name,
            attachments=[
                mattermost.Attachment(
                    text=request.data.description_text.replace("\\n", "\n"),
                    title=request.data.description_title,
                    fallback="Metric Alert reported by Sentry: " + request.actor.name,
                    color="#ffff00",
                    author_name="Sentry",
                    author_icon=icon_path,
                    author_link="test_link",
                    title_link=request.data.web_url,
                    fields=[
                        mattermost.Field(
                            short=True,
                            title="Alert Title",
                            value=request.data.metric_alert.alert_rule.name,
                        ),
                        mattermost.Field(
                            short=True,
                            title="Projects",
                            value=", ".join(request.data.metric_alert.alert_rule.projects),
                        ),
                    ],
                ),
            ]
        )
