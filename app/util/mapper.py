import string

from app import mattermost, sentry


class WebhookMapper:
    @staticmethod
    def map_event_alert(
            request: sentry.EventAlertWebhook,
            icon_path: str = "https://assets.stickpng.com/images/58482eedcef1014c0b5e4a76.png"
    ) -> mattermost.IncomingWebhook:
        return mattermost.IncomingWebhook(
            username="Sentry",
            attachments=[
                mattermost.Attachment(
                    text=request.data.event.metadata.value or request.data.event.title,
                    title=request.data.event.title,
                    fallback="Issue Alert reported by Sentry: " + request.actor.name,
                    color="#FF0000",
                    author_name="Sentry",
                    author_icon=icon_path,
                    title_link=request.data.event.web_url,
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
            username="Sentry",
            attachments=[
                mattermost.Attachment(
                    text=request.data.description_text.replace("\\n", "\n"),
                    title=request.data.description_title,
                    fallback="Metric Alert reported by Sentry: " + request.actor.name,
                    color="#ffff00",
                    author_name="Sentry",
                    author_icon=icon_path,
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


@staticmethod
def map_default(
        request: sentry.Webhook,
        subject: sentry.SentryHookResource,
        icon_path: str = "https://assets.stickpng.com/images/58482eedcef1014c0b5e4a76.png"
) -> mattermost.IncomingWebhook:
    if "web_url" in request.data.keys():
        web_url = request.data["web_url"]
    elif "web_url" in request.data[subject].keys():
        web_url = request.data[subject]["web_url"]
    else:
        web_url = ""
    return mattermost.IncomingWebhook(
        username="Sentry",
        attachments=[
            mattermost.Attachment(
                text=request.data[subject]["title"] + "@" + request.data[subject]["culprit"],
                title=string.Template("$type $action by: $name").substitute(type=subject.value,
                                                                            action=request.action,
                                                                            name=request.actor.name)
                ,
                color="#4cb9fa",
                author_name="Sentry",
                author_icon=icon_path,
                title_link=web_url,
            ),
        ]
    )
