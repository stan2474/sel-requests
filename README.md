# sel-requests
A selenium-based requests module for evading TLS fingerprinting in Python.

## Pros
- Bypass JA3 fingerprinting
- Uses `fetch()` to send requests, thus no page rendering is done

## Cons
- Relatively long init times
- No control over cookies
- No control over redirects
- All other limits of fetch(), except for CORS/SOP

# Setup
```bash
pip install -U git+https://github.com/h0nde/sel-requests.git
```

# Usage
```python3
import selrequests

with selrequests.Session() as s:
  resp = s.get("https://ja3er.com/json")
  print(resp.json())
```

# Documentation

### Session(proxy_url=None, user_agent=DEFAULT)
Creates a requests-like session

### Session.request(method, url, data, json, headers)

### Session.get, .post, .put, .patch, .delete

### Session.set_origin(url)
Sets the instance's current page url, useful for setting Referer/Origin/Sec-Fetch headers.

### Session.close()
Closes the selenium instance.
