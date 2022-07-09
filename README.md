# `twitter-chucknorris-aws` [![Lint](https://github.com/gideonshaked/twitter-chucknorris-aws/workflows/Lint/badge.svg)](https://github.com/gideonshaked/twitter-chucknorris-aws/actions?query=workflow%3ALint)

This is a Twitter bot hosted on AWS Lambda that posts Chuck Norris jokes on a schedule. You can check it out at [https://twitter.com/chucknorrisbot1](https://twitter.com/chucknorrisbot1).

## Architecture

Chuck Norris Bot runs as an AWS Lambda function that solely consists of [`twitter_chucknorris.py`](https://github.com/gideonshaked/twitter-chucknorris-aws/blob/master/src/twitter_chucknorris.py). It is triggered by an Amazon Eventbridge Rule that runs on a cron schedule of every three hours from 9:00 am to 6:00 pm every day. It also utilizes a Lambda layer to pull in its dependencies—[Tweepy](https://github.com/tweepy/tweepy) and [Requests](https://github.com/psf/requests).
