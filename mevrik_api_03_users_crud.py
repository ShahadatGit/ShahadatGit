

import requests
import json
import pytest
from mevrik_api_01_host_check import host_url


token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5NDM3NjUzLCJqdGkiOiJlNzcxMTAxODNiZjg0NDFhYjMxNWNkMzM0Yzk3ZWYwMiIsInVzZXJfaWQiOjR9.ly_CtbMxLkArtDxrcgO2TrM-sWy8jvk46FURbIlCnkA"
header = {
        "content-type":"application/json",
        "Authorization":"Bearer " + token,
        "Cache-Control": "no-cache"
        }
datapost = {"password": "123456","email": "pytest1@example.com","first_name": "pytester","last_name": "shahadat","role_id": 2}
dataput = {"password": "654321","email": "pytest2@example.com","first_name": "pytest one","last_name": "python","role_id": 3}

def test_read_all_user_status_code_equals_200():
    response=requests.get(host_url + "users/", headers=header)
    print(response)
    assert response.status_code == 200

def test_read_single_user_status_code_equals_200():
    response = requests.get(host_url + "users/4/", headers=header)
    print(response)
    assert response.status_code == 200

#def test_create_single_user_status_code_equals_201():
#    response = requests.post(host_url + "users/", data=json.dumps(datapost), headers=header)
#    assert response.status_code == 201

#def test_update_single_user_status_code_equals_200():
#    response = requests.put(host_url + "users/11/", data=json.dumps(dataput), headers=header)
#    assert response.status_code == 200

#def test_delete_single_user_status_code_equals_204():
#    response = requests.delete(host_url + "users/11/", headers=header, timeout=2.5)
#    assert response.status_code == 204

test_read_all_user_status_code_equals_200()
test_read_single_user_status_code_equals_200()

#test_create_single_user_status_code_equals_201()
#test_update_single_user_status_code_equals_200()
#test_delete_single_user_status_code_equals_204()