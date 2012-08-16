#!/usr/bin/env python

"""
grequests + oauth = <3
"""

import grequests, requests

from oauth_hook import OAuthHook

def grequests_oauth_client(access_token=None, access_token_secret=None, consumer_key=None, consumer_secret=None, header_auth=None):
    oauth_hook = OAuthHook(access_token=access_token, access_token_secret=access_token_secret, 
                           consumer_key=consumer_key, consumer_secret=consumer_secret, 
                           header_auth=header_auth)

    client = requests.session(hooks={'pre_request': oauth_hook})

    client.get = grequests.patched(client.get)
    client.options = grequests.patched(grequests.options)
    client.head = grequests.patched(grequests.head)
    client.post = grequests.patched(grequests.post)
    client.put = grequests.patched(grequests.put)
    client.patch = grequests.patched(grequests.patch)
    client.delete = grequests.patched(grequests.delete)
    client.request = grequests.patched(grequests.request)

    return client
