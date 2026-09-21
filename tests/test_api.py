import requests
from framework.decorators import test

@test("API Health Check", timeout=5)
def api_health():

    r = requests.get("https://httpbin.org/status/200")

    assert r.status_code == 200