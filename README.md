# Sentry Mattermost Proxy

---
A proxy server for integrating Sentry 21 alerts into Incoming Webhooks on Mattermost.

## Overview

- This project is a proxy server designed to seamlessly integrate Sentry 21 alerts into Incoming Webhooks on Mattermost,
  a popular team collaboration platform. With this proxy server, you can receive real-time alerts from Sentry 21
  directly into your Mattermost channels, keeping your team informed and enabling swift response to critical issues.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## [Installation](#installation)

Follow these steps to set up the Sentry 21 to Mattermost Proxy Server:

- Prerequisites:
    - Python (version >= 3.11)
    - Docker
- Clone the repository

```sh
git clone https://github.com/copolio/sentry-mattermost-proxy.git
```

- Deploy FastAPI application

Dockerfile is provided in the repository for your convenience.

```sh
docker build -t sentry-mattermost-proxy .
docker run -d --name sentry-mattermost-proxy -p 80:80 sentry-mattermost-proxy
```

Your Sentry 21 to Mattermost proxy server is now running and ready to forward alerts to Mattermost.

## [Usage](#usage)

Once the proxy server is operational, configuring Sentry 21 to send alerts is a breeze:

1. Create an Incoming Webhook URL in your Mattermost instance.

2. Modify the host portion of your generated webhook URL (e.g., http://your-proxy-server-url:
   port/hooks/{generated_webhook_key}).

3. Specify custom alert rules with the webhook URL in Sentry 21's alerting settings.

The proxy server will seamlessly relay these alerts to the designated Mattermost channel.

## [Contributing](#contributing)

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Commit your changes and create a pull request.

Please ensure that your code adheres to the project's coding standards and includes relevant tests if applicable.

## [License](#license)

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
