requestsimple
=============

A simple HTTP cookielib helper

Usage:
======

1. Get
````
    req = session()
    res = get(req, "https://myurl/")
    print res.read()
````
2. Post
````
    req = session()
    res = post(req, "https://myurl/", {"user":"myuser", "password":"mypassword"})
    print res.read()
    
    ## perform more requests after login
    res = get(req, "https://myurl/myroute/")
    print res.read()
````
