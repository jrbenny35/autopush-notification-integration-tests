# Autopush Notification Integration Tests

## About

Notification in Firefox are a crucial part of its functionality. Firefox uses [autopush] for this. This repo contains a set of tests to check the functionaility of thhese notifications.

## Technology

The tests use [Selenium], [pytest], [docker] as well as Firefox.

## Getting Started

Make sure you have installed [docker-compose] as well as Docker.

```sh
docker-compose up --build -d
docker-compose exec --user root firefox mkdir images/
docker-compose exec firefox pip3 install --user -r requirements.txt
docker-compose exec firefox python3 -m pytest --driver Firefox --env dev
```

### Command line options

```--env``` : stage, dev, prod. This controls the URL that is set for the push server.
- stage: wss://autopush.stage.mozaws.net
- dev: wss://autopush.dev.mozaws.net/
- prod: wss://push.services.mozilla.com/