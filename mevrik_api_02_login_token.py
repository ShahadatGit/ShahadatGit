import requests
import json
from mevrik_api_01_host_check import host_url
from pprint import pprint

header = {
  "Content-Type": "application/json",
  "Cache-Control": "no-cache"
}
payload = json.dumps({
  "email": "shahadat.hossain@genex.digital",
  "password": "0037"
})

def test_login_token_status_code_equals_200():
    response=requests.post(host_url + "/api/token/", headers=header, data=payload)
    data = response.json()
    access = data["access"]
    assert response.status_code == 200
    return access

# access = test_login_token_status_code_equals_200()
# pprint(access)

token = None
def get_token():
  global token
  if token is None:
    token = test_login_token_status_code_equals_200()
  return token 

