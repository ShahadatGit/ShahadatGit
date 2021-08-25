
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
datapost = json.dumps({"preferred_language": "English", "user_id": 11})
dataput = json.dumps({"preferred_language": "Bengali", "user_id": 4})

def test_read_all_user_profile_status_code_equals_200():
    response=requests.get(host_url + "/user_profiles/", headers=header)
    print(response)
    assert response.status_code == 200

def test_read_single_user_profile_status_code_equals_200():
    response = requests.get(host_url + "/user_profiles/2/", headers=header)
    print(response)
    assert response.status_code == 200

def test_create_single_user_profile_status_code_equals_201():
    response = requests.post(host_url + "/user_profiles/", headers=header, data=datapost)
    print(response)
    assert response.status_code == 201

def test_update_single_user_profile_status_code_equals_200():
    response = requests.put(host_url + "/user_profiles/4/", headers=header, data=dataput)
    print(response)
    assert response.status_code == 200

def test_delete_single_user_profile_status_code_equals_204():
    response = requests.delete(host_url + "/user_profiles/5/", headers=header, timeout=2.5)
    print(response)
    assert response.status_code == 204

test_read_all_user_profile_status_code_equals_200()
test_read_single_user_profile_status_code_equals_200()
test_create_single_user_profile_status_code_equals_201()
test_update_single_user_profile_status_code_equals_200()
test_delete_single_user_profile_status_code_equals_204()