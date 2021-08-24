
import requests
from myconf import host_url
#host_url = "https://reqres.in/api/users?page=2"
url = host_url
def test_host_check_status_code_equals_200():
    response = requests.get(host_url)
    print(response)
    assert response.status_code == 200

test_host_check_status_code_equals_200()
