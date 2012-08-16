#!/usr/bin/env python

"""
grequests + oauth = <3
"""

import grequests, requests

from oauth_hook import OAuthHook

def grequests_oauth_client(access_token=None, access_token_secret=None, consumer_key=None, consumer_secret=None, header_auth=None, **kwargs):
    oauth_hook = OAuthHook(access_token=access_token, access_token_secret=access_token_secret, 
                           consumer_key=consumer_key, consumer_secret=consumer_secret, 
                           header_auth=header_auth)

    # TODO: support other hooks passed in via kwargs

    client = requests.session(hooks={'pre_request': oauth_hook})

    client.get = grequests.patched(client.get)
    client.options = grequests.patched(client.options)
    client.head = grequests.patched(client.head)
    client.post = grequests.patched(client.post)
    client.put = grequests.patched(client.put)
    client.patch = grequests.patched(client.patch)
    client.delete = grequests.patched(client.delete)
    client.request = grequests.patched(client.request)

    return client
