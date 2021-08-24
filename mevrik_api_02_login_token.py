import requests
import json
from mevrik_api_01_host_check import host_url


header = {
  "Content-Type": "application/json",
  "Cache-Control": "no-cache"
}
payload = json.dumps({
  "email": "shahadat.hossain@genex.digital",
  "password": "0037"
})

def test_login_token_status_code_equals_201():
    response=requests.post(host_url + "api/token/", headers=header, data=payload)
    assert response.status_code == 201
    return [response]
