# Autopush Notification Integration Tests

## About

Notification in Firefox are a crucial part of its functionality. Firefox uses [autopush](https://github.com/mozilla-services/autopush) for this. This repo contains a set of tests to check the functionaility of thhese notifications.

## Technology

The tests use [Selenium](https://www.selenium.dev/), [pytest](https://docs.pytest.org/en/stable/index.html), [docker](https://www.docker.com/) as well as Firefox.

## Getting Started

Make sure you have installed [docker-compose](https://docs.docker.com/compose/) as well as Docker.

```sh
docker-compose up --build -d
docker-compose exec firefox pip3 install --user -r requirements.txt
docker-compose exec firefox python3 -m pytest --driver Firefox --env dev
```

### Command line options

```--env``` : stage, dev, prod. This controls the URL that is set for the push server.
- stage: wss://autopush.stage.mozaws.net
- dev: wss://autopush.dev.mozaws.net/
- prod: wss://push.services.mozilla.com/