from unittest import TestCase

from app.mattermost import IncomingWebhook


class TestIncomingWebhook(TestCase):
    def test_request_deserialize_success(self):
        # given
        json_dict = {
            "channel": "town-square",
            "username": "Winning-bot",
            "text": "#### We won a new deal!",
            "props": {
                "card": "Salesforce Opportunity Information:\n\n [Opportunity Name]("
                        "https://salesforce.com/OPPORTUNITY_ID)\n\n-Salesperson: **Bob McKnight** \n\n Amount: "
                        "**$300,020.00**"
            }
        }
        # when
        incoming_webhook = IncomingWebhook.model_validate(json_dict)
        # then
        self.assertEquals(json_dict.get("channel"), incoming_webhook.channel)
        self.assertEquals(json_dict.get("username"), incoming_webhook.username)
        self.assertEquals(json_dict.get("text"), incoming_webhook.text)
        self.assertEquals(json_dict.get("props"), incoming_webhook.props)

    pass
