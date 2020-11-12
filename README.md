# selenium-requests
Lame work-around for bypassing JA3 fingerprinting websites in Python.

## Pros
- Bypass JA3 fingerprinting

## Pros over cryzed/Selenium-Requests
- No actual page rendering is done, apart from .set_page

## Cons
- Selenium-based
- No control over cookie handling
- No control over redirects

# Usage
```python3
import selrequests

with selrequests.Session() as s:
  resp = s.get("https://ja3er.com/json")
  print(resp.json())
```

# Documentation

## Session(proxy_url=None)
Creates a requests-like session

## Session.request(method, url, data, json, headers)

## Session.get, .post, .put, .patch, .delete

## Session.set_origin(url)
Sets the instance's current page url, without actually visiting it.

## Session.set_page(url)
Sets the instance's current page url by visiting it.

## Session.close()
Closes the selenium instance.
