# selenium-requests
Lame work-around for bypassing JA3 fingerprinting websites.

## Pros
- Bypass JA3 fingerprinting

## Cons
- Selenium-based
- No control over cookie handling
- No control over redirects

# Usage
```python3
import sel_requests

with sel_requess.Session() as s:
  resp = s.get("https://ja3er.com/json")
  print(resp.text)
```

# Documentation

## Session(proxy_url=None)
Creates a requests-like session

## Session.request(method, url, data, json, headers)

## Session.get, .post, .put, .patch, .delete

## Session.set_page(url)
Sets the selenium instance's current page url.

## Session.close()
Closes the selenium instance.
