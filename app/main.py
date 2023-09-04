from fastapi import FastAPI, Header, HTTPException
from fastapi.requests import Request
from fastapi.responses import RedirectResponse, ORJSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from httpx import AsyncClient

from app import sentry, util

app = FastAPI(
    title="Sentry Mattermost Proxy",
    summary="Proxy endpoint for Sentry Alerts to Mattermost Incoming webhook request",
)
app.mount("/static", StaticFiles(directory="static"), name="static")
client = AsyncClient()


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post(
    path="/{mattermost_host}/hooks/{key}",
    status_code=201,
    description="Formats and redirects Sentry webhook alerts to Mattermost Incoming Webhook",
    tags=["webhooks"],
)
async def hooks(
        mattermost_host: str,
        key: str,
        sentry_webhook: sentry.Webhook,
        request: Request,
        use_https: bool = False,
        sentry_hook_resource: sentry.AlertType = Header(default=sentry.AlertType.Issue,
                                                        alias="Sentry-Hook-Resource"),
):
    """
    Use this endpoint to send a Sentry webhook payload to be processed and forwarded to Mattermost.
    """
    url = request.url
    icon_path = url.scheme + "://" + url.netloc + "/static/images/thumbnail.png"

    if sentry_hook_resource == sentry.AlertType.Issue:
        issue_alert_webhook = sentry.IssueAlertWebhook.model_validate(sentry_webhook.model_dump())
        mattermost_webhook = util.WebhookMapper.map_issue_alert(
            request=issue_alert_webhook,
            icon_path=icon_path,
        )
    elif sentry_hook_resource == sentry.AlertType.Metric:
        metric_alert_webhook = sentry.MetricAlertWebhook.model_validate(sentry_webhook.model_dump())
        mattermost_webhook = util.WebhookMapper.map_metric_alert(
            request=metric_alert_webhook,
            icon_path=icon_path
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid hook resource")

    protocol = "https://" if use_https else "http://"
    response = await client.post(
        url=protocol + mattermost_host + "/hooks/" + key,
        json=mattermost_webhook.model_dump())

    if response.is_success:
        sentry_response = PlainTextResponse(content=response.content,
                                            status_code=response.status_code)
    else:
        sentry_response = ORJSONResponse(content=response.json(),
                                         status_code=response.status_code)
    return sentry_response
