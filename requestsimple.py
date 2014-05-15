#!/usr/bin/env python
""" requestsimple.py
A simple http cookielib helper

Usage:

1. Get:
    req = session()
    res = get(req, "https://myurl/")
    print res.read() ## returns the content

2. Post:
    req = session()
    res = post(req, "https://myurl/", {"user":"myuser", "password":"mypassword"})
    print res.read() ## returns the content after logging if __name__ == '__main__':

    ## perform more requests after login
    res = get(req, "https://myurl/myroute/")
    print res.read() ## returns the content

"""

import urllib
import urllib2
import cookielib


def session():
    cj = cookielib.CookieJar()
    return urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


def get(req, url):
    return _get_response(req, url)


def post(req, url, values=None):
    return _get_response(req, url, values)


def _get_response(req, url, values=None):
    res = None

    if values:
        data = urllib.urlencode(values)
        res = req.open(url, data)
    else:
        res = req.open(url)

    return res


if __name__ == "__main__":

    values = {'login': 'myuser', 'password': 'mypassword'}
    myurl = 'https://server/'

    req = session()

    res = get(req, myurl)
    print res.read()

    res = post(req, myurl, values)
    print res.read()

    res = get(req, myurl + "trade/")
    print res.read()
