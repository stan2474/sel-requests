from selenium import webdriver
from requests.structures import CaseInsensitiveDict
from urllib.parse import urlencode
import json as _json

with open(__file__ + "/../" + "js/request.js") as f:
    js_request_template = f.read()

def create_chrome_options(proxy_url=None):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-web-security")
    if proxy_url:
        options.add_argument(f"--proxy-server={proxy_url}")
    return options

class Request:
    def __init__(self, method, url, data=None,
                 json=None, headers=None):
        self.headers = CaseInsensitiveDict(headers)
        self.method = method
        self.url = url

        if json:
            self.headers["Content-Type"] = "application/json; charset=UTF-8"
            self.data = _json.dumps(json, separators=(",",":"))
        
        elif type(data) == dict:
            self.headers["Content-Type"] = "application/x-www-form-urlencoded"
            self.data = urlencode(data)
        
        else:
            self.data = data
    
class Response:
    def __init__(self, url, text, headers, status_code, reason, ok):
        self.url = url
        self.ok = ok
        self.status_code = status_code
        self.reason = reason
        self.text = text
        self.content = text.encode("UTF-8")
        self.headers = CaseInsensitiveDict(headers)

    def __repr__(self):
        return "<Response [%d]>" % self.status_code

    def json(self):
        return _json.loads(self.text)

class Session:
    def __init__(self, proxy_url=None):
        self.headers = {}
        self._webdriver = webdriver.Chrome(
            options=create_chrome_options(proxy_url)
        )

    def __enter__(self):
        return self
    
    def __exit__(self, *_):
        self.close()

    def close(self):
        self._webdriver.quit()

    def set_page(self, url):
        self._webdriver.get(url)

    def send(self, request):
        headers = dict(request.headers)
        headers.update(self.headers)
        resp = Response(**self._webdriver.execute_script(
            js_request_template,
            request.method,
            request.url,
            request.data,
            headers
        ))
        return resp

    def request(self, *v, **kw):
        req = Request(*v, **kw)
        resp = self.send(req)
        return resp

    def get(self, *v, **kw):
        return self.request("GET", *v, **kw)

    def post(self, *v, **kw):
        return self.request("POST", *v, **kw)

    def put(self, *v, **kw):
        return self.request("PUT", *v, **kw)

    def patch(self, *v, **kw):
        return self.request("PATCH", *v, **kw)

    def delete(self, *v, **kw):
        return self.request("DELETE", *v, **kw)