
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
datapost = json.dumps({"password": "123456","email": "pytest@example.com","first_name": "pytester","last_name": "shahadat","role_id": 2})
dataput = json.dumps({"password": "654321","email": "pytest2@example.com","first_name": "pytest one","last_name": "python","role_id": 3})

def test_read_all_user_status_code_equals_200():
    response=requests.get(host_url + "/users/", headers=header)
    print(response)
    assert response.status_code == 200

def test_read_single_user_status_code_equals_200():
    response = requests.get(host_url + "/users/2/", headers=header)
    pprint(response.json())
    assert response.status_code == 200

def test_create_single_user_status_code_equals_201():
    response = requests.post(host_url + "/users/", headers=header, data=datapost)
    print(response)
    assert response.status_code == 201

def test_update_single_user_status_code_equals_200():
    response = requests.put(host_url + "/users/13/", headers=header, data=dataput)
    print(response)
    assert response.status_code == 200

def test_delete_single_user_status_code_equals_204():
    response = requests.delete(host_url + "/users/11/", headers=header, timeout=2.5)
    print(response)
    assert response.status_code == 204


test_read_all_user_status_code_equals_200()
test_read_single_user_status_code_equals_200()
test_create_single_user_status_code_equals_201()
test_update_single_user_status_code_equals_200()
test_delete_single_user_status_code_equals_204()