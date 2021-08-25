
import requests
import json
from mevrik_api_01_host_check import host_url
from mevrik_api_02_login_token import get_token
from pprint import pprint 


token = get_token()
header = {
        "content-type":"application/json",
        "Authorization":"Bearer " + token,
        "Cache-Control": "no-cache"
        }
datapost = json.dumps({"name": "Customer new"})
dataput = json.dumps({"name": "Customer update"})

def test_read_all_customer_status_code_equals_200():
    response=requests.get(host_url + "/customers/", headers=header)
    print(response)
    assert response.status_code == 200

def test_read_single_customer_status_code_equals_200():
    response = requests.get(host_url + "/customers/2/", headers=header)
    print(response)
    assert response.status_code == 200

def test_create_single_customer_status_code_equals_201():
    response = requests.post(host_url + "/customers/", headers=header, data=datapost, timeout=2.5)
    print(response)
    assert response.status_code == 201

def test_update_single_customer_status_code_equals_200():
    response = requests.put(host_url + "/customers/3/", headers=header, data=dataput, timeout=2.5)
    print(response)
    assert response.status_code == 200

def test_delete_single_customer_status_code_equals_204():
    response = requests.delete(host_url + "/customers/3/", headers=header, timeout=2.5)
    print(response)
    assert response.status_code == 204

test_read_all_customer_status_code_equals_200()
test_read_single_customer_status_code_equals_200()
test_create_single_customer_status_code_equals_201()
test_update_single_customer_status_code_equals_200()
test_delete_single_customer_status_code_equals_204()