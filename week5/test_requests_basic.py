import requests
import pytest

#测试GET请求
def test_get_request():
    """测试GET请求"""
    url = "https://httpbin.org/get"
    params = {'name':"test","age":15}

    response = requests.get(url,params=params)

    assert response.status_code == 200
    assert response.json()["args"]["name"] == "test"
    print(f"\n响应:{response.json()}")

#测试POST请求（表单）
def test_post_form():
    url = "https://httpbin.org/post"
    data = {"username":"cg12","password":"123456"}

    response = requests.post(url,data=data)

    assert response.status_code == 200
    assert response.json()["form"]["username"] == "cg12"
    print(f"\n响应:{response.json()['form']}")

#模拟POST请求（json）
def test_post_json():
    url = "https://httpbin.org/post"
    json_data = {"title":"测试","contene":"接口自动化"}

    response = requests.post(url,json=json_data)

    assert response.status_code == 200
    assert response.json()["json"]["title"] == '测试'
    print(f"\n响应:{response.json()['json']}")

#模拟请求头
def test_with_headers():
    url = "https://httpbin.org/headers"
    headers = {
        "User-Agent":"pytest-automation/1.0",
        "Authorization":"Bearer token123"
    }

    response = requests.get(url,headers=headers)

    assert response.status_code == 200
    assert "pytest-automation" in response.json()["headers"]["User-Agent"]
    print(f"\n响应头: {response.json()['headers']}")

#测试超时
def test_timeout():
    url = "https://httpbin.org/delay/5"

    #设置3秒超时，应该抛出异常
    with pytest.raises(requests.exceptions.Timeout):
        requests.get(url,timeout=3)
    print("\n超时测试通过")