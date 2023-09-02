from typing import cast

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from httpx import AsyncClient

from app import sentry, util

app = FastAPI(
    title="Sentry Mattermost Proxy",
    summary="Proxy endpoint for Sentry Alerts to Mattermost Incoming webhook request",
)
client = AsyncClient()


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post(
    path="/:mattermost_host/hooks/:key",
    status_code=201,
    description="Formats and redirects Sentry webhook alerts to Mattermost Incoming Webhook",
    tags=["webhooks"],
)
async def hooks(
        mattermost_host: str,
        key: str,
        sentry_webhook: sentry.Webhook,
        sentry_hook_resource: sentry.AlertType | None = Header(default=sentry.AlertType.Issue)
):
    """
    Use this endpoint to send a Sentry webhook payload to be processed and forwarded to Mattermost.
    """

    if sentry_hook_resource == sentry.AlertType.Issue:
        request = util.WebhookMapper.map_issue_alert(cast(sentry.IssueAlertWebhook, sentry_webhook))
    elif sentry_hook_resource == sentry.AlertType.Metric:
        # TODO
        raise HTTPException(status_code=501, detail="Currently Unsupported")
        # request = util.WebhookMapper.map_metric_alert(cast(sentry.MetricAlertWebhook, sentry_webhook))
    else:
        raise HTTPException(status_code=400, detail="Invalid hook resource")

    response = await client.post(
        url="https://" + mattermost_host + "/hooks/" + key,
        data=request.model_dump())

    return JSONResponse(content=response, status_code=201)
