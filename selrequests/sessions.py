from .structures import Request, Response
from selenium import webdriver
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
with open(__file__ + "/../" + "js/request.js") as f:
    js_request_template = f.read()

def create_chrome_options(proxy_url=None, user_agent=USER_AGENT):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--log-level=3")
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--headless")
    options.add_argument("--disable-web-security")
    if proxy_url:
        options.add_argument(f"--proxy-server={proxy_url}")
    return options

class Session:
    def __init__(self, proxy_url=None, user_agent=USER_AGENT):
        self.user_agent = user_agent
        self.headers = {}
        self._webdriver = webdriver.Chrome(
            options=create_chrome_options(proxy_url, self.user_agent),
            service_log_path="NUL"
        )

    def __enter__(self):
        return self
    
    def __exit__(self, *_):
        self.close()

    def close(self):
        self._webdriver.quit()

    def set_origin(self, url):
        self._webdriver.execute_script(
            "history.replaceState(null, null, arguments[0])",
            url
        )

    def set_page(self, url):
        self._webdriver.get(url)

    def send(self, request):
        headers = dict(self.headers)
        headers.update(request.headers)
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
