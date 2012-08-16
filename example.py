#!/usr/bin/env python

"""
Example of using grequests with OAuth.

See: https://github.com/kennethreitz/grequests
"""

import json

import grequests

from grequests_oauth import grequests_oauth_client

import settings

def example():
    client = grequests_oauth_client(access_token=settings.OAUTH_TOKEN, access_token_secret=settings.OAUTH_SECRET, 
                                    consumer_key=settings.CONSUMER_KEY, consumer_secret=settings.CONSUMER_SECRET, 
                                    header_auth=False)

    urls = 5 * ['http://api.twitter.com/1/account/rate_limit_status.json']
    rs = (client.get(u) for u in urls)

    return [json.loads(response.content) for response in grequests.map(rs)]

if __name__ == "__main__":
    print example()