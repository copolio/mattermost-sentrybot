from unittest import TestCase

from app.sentry import IssueAlertWebhook


class TestIssueAlertWebhook(TestCase):
    def test_request_deserialize_success(self):
        # given
        json_dict = {
            "action": "triggered",
            "actor": {
                "id": "sentry",
                "name": "Sentry",
                "type": "application"
            },
            "data": {
                "event": {
                    "_ref": 1,
                    "_ref_version": 2,
                    "contexts": {
                        "browser": {
                            "name": "Chrome",
                            "type": "browser",
                            "version": "75.0.3770"
                        },
                        "os": {
                            "name": "Mac OS X",
                            "type": "os",
                            "version": "10.14.0"
                        }
                    },
                    "culprit": "?(<anonymous>)",
                    "datetime": "2019-08-19T21:06:17.677000Z",
                    "dist": None,
                    "event_id": "e4874d664c3540c1a32eab185f12c5ab",
                    "exception": {
                        "values": [
                            {
                                "mechanism": {
                                    "data": {
                                        "message": "heck is not defined",
                                        "mode": "stack",
                                        "name": "ReferenceError"
                                    },
                                    "description": None,
                                    "handled": False,
                                    "help_link": None,
                                    "meta": None,
                                    "synthetic": None,
                                    "type": "onerror"
                                },
                                "stacktrace": {
                                    "frames": [
                                        {
                                            "abs_path": "https://static.jsbin.com/js/prod/runner-4.1.7.min.js",
                                            "colno": 10866,
                                            "context_line": "{snip} e(a.old),a.active=b,e(a.target,b),setTimeout(function(){c&&c();for(var b,d=a.target.getElementsByTagName(\"iframe\"),e=d.length,f=0,g=a.active {snip}",
                                            "data": {
                                                "orig_in_app": 1
                                            },
                                            "errors": None,
                                            "filename": "/js/prod/runner-4.1.7.min.js",
                                            "function": None,
                                            "image_addr": None,
                                            "in_app": False,
                                            "instruction_addr": None,
                                            "lineno": 1,
                                            "module": "prod/runner-4.1.7",
                                            "package": None,
                                            "platform": None,
                                            "post_context": None,
                                            "pre_context": None,
                                            "raw_function": None,
                                            "symbol": None,
                                            "symbol_addr": None,
                                            "trust": None,
                                            "vars": None
                                        },
                                        {
                                            "abs_path": "https://static.jsbin.com/js/prod/runner-4.1.7.min.js",
                                            "colno": 13924,
                                            "context_line": "{snip} e){i._raw(\"error\",e&&e.stack?e.stack:a+\" (line \"+c+\")\")},c.write(f),c.close(),b.postMessage(\"complete\"),k.wrap(e,a.options)})},b[\"console:ru {snip}",
                                            "data": {
                                                "orig_in_app": 1
                                            },
                                            "errors": None,
                                            "filename": "/js/prod/runner-4.1.7.min.js",
                                            "function": None,
                                            "image_addr": None,
                                            "in_app": False,
                                            "instruction_addr": None,
                                            "lineno": 1,
                                            "module": "prod/runner-4.1.7",
                                            "package": None,
                                            "platform": None,
                                            "post_context": None,
                                            "pre_context": None,
                                            "raw_function": None,
                                            "symbol": None,
                                            "symbol_addr": None,
                                            "trust": None,
                                            "vars": None
                                        },
                                        {
                                            "abs_path": "<anonymous>",
                                            "colno": 5,
                                            "context_line": None,
                                            "data": {
                                                "orig_in_app": 1
                                            },
                                            "errors": None,
                                            "filename": "<anonymous>",
                                            "function": None,
                                            "image_addr": None,
                                            "in_app": False,
                                            "instruction_addr": None,
                                            "lineno": 3,
                                            "module": None,
                                            "package": None,
                                            "platform": None,
                                            "post_context": None,
                                            "pre_context": None,
                                            "raw_function": None,
                                            "symbol": None,
                                            "symbol_addr": None,
                                            "trust": None,
                                            "vars": None
                                        }
                                    ]
                                },
                                "type": "ReferenceError",
                                "value": "heck is not defined"
                            }
                        ]
                    },
                    "fingerprint": ["{{ default }}"],
                    "grouping_config": {
                        "enhancements": "eJybzDhxY05qemJypZWRgaGlroGxrqHRBABbEwcC",
                        "id": "legacy:2019-03-12"
                    },
                    "hashes": ["29f7ffc4903a8a990408b80a3b4c95a2"],
                    "issue_url": "https://sentry.io/api/0/issues/1117540176/",
                    "issue_id": "1117540176",
                    "key_id": "667532",
                    "level": "error",
                    "location": "<anonymous>",
                    "logger": "",
                    "message": "",
                    "metadata": {
                        "filename": "<anonymous>",
                        "type": "ReferenceError",
                        "value": "heck is not defined"
                    },
                    "platform": "javascript",
                    "project": 1,
                    "received": 1566248777.677,
                    "release": None,
                    "request": {
                        "cookies": None,
                        "data": None,
                        "env": None,
                        "fragment": None,
                        "headers": [
                            [
                                "User-Agent",
                                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
                            ]
                        ],
                        "inferred_content_type": None,
                        "method": None,
                        "query_string": [],
                        "url": "https://None.jsbin.com/runner"
                    },
                    "sdk": {
                        "integrations": [
                            "InboundFilters",
                            "FunctionToString",
                            "TryCatch",
                            "Breadcrumbs",
                            "GlobalHandlers",
                            "LinkedErrors",
                            "HttpContext"
                        ],
                        "name": "sentry.javascript.browser",
                        "packages": [
                            {
                                "name": "npm:@sentry/browser",
                                "version": "5.5.0"
                            }
                        ],
                        "version": "5.5.0"
                    },
                    "tags": [
                        ["browser", "Chrome 75.0.3770"],
                        ["browser.name", "Chrome"],
                        ["handled", "no"],
                        ["level", "error"],
                        ["mechanism", "onerror"],
                        ["os", "Mac OS X 10.14.0"],
                        ["os.name", "Mac OS X"],
                        ["user", "ip:162.217.75.90"],
                        ["url", "https://None.jsbin.com/runner"]
                    ],
                    "time_spent": None,
                    "timestamp": 1566248777.677,
                    "title": "ReferenceError: heck is not defined",
                    "type": "error",
                    "url": "https://sentry.io/api/0/projects/test-org/front-end/events/e4874d664c3540c1a32eab185f12c5ab/",
                    "user": {
                        "ip_address": "162.218.85.90"
                    },
                    "version": "7",
                    "web_url": "https://sentry.io/organizations/test-org/issues/1117540176/events/e4874d664c3540c1a32eab185f12c5ab/"
                },
                "triggered_rule": "Very Important Alert Rule!",
                "issue_alert": {
                    "title": "Very Important Alert Rule!",
                    "settings": [
                        {
                            "name": "channel",
                            "value": "#general"
                        }
                    ]
                }
            },
            "installation": {
                "uuid": "a8e5d37a-696c-4c54-adb5-b3f28d64c7de"
            }
        }
        # when
        issue_alert_webhook = IssueAlertWebhook.model_validate(json_dict)
        # then
        self.assertEquals(json_dict.get("action"), issue_alert_webhook.action)

    pass
