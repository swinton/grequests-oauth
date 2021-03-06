# GRequests + OAuth: Asynchronous, OAuth'd HTTP requests

GRequests + OAuth allows you to make asynchronous, OAuth'd HTTP requests easily.

Magic courtesy of [GRequests](https://github.com/kennethreitz/grequests) and [requests-oauth](https://github.com/maraujop/requests-oauth).

## Usage

See [example.py](https://github.com/swinton/grequests-oauth/blob/master/example.py).

Basically:

    import grequests

    from grequests_oauth import grequests_oauth_client

    client = grequests_oauth_client(access_token, access_token_secret, 
                                    consumer_key, consumer_secret, 
                                    header_auth)

    urls = 5 * ['http://api.twitter.com/1/account/rate_limit_status.json']

Create a set of unsent Requests:

    >>> rs = (client.get(u) for u in urls)

Send them all at the same time:

    >>> grequests.map(rs)
    [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>]

## Installation

Clone:

    $ git clone git://github.com/swinton/grequests-oauth.git .

Install requirements:

    $ pip install -r requirements.txt


