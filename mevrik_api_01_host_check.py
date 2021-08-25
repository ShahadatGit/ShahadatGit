
import requests

host_url = "https://genexdigital.com"


def test_host_check_status_code_equals_200():    
    response = requests.get(host_url)
    print(response)
    assert response.status_code == 200

test_host_check_status_code_equals_200()
