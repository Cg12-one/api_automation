import requests
import pytest
import json

#测试文件上传
def test_file_upload():
    url = "https://httpbin.org/post"

    #创建临时文件
    files = {"file":("test.txt","这是测试内容","text/plain")}

    response = requests.post(url,files=files)

    assert response.status_code == 200
    # assert "test.txt" in response.json()["files"]
    assert "file" in response.json()["files"]  # ✅ 验证字段名
    assert response.json()["files"]["file"] == "这是测试内容"  # ✅ 验证内容
    print(f"\n上传响应：{response.json()['files']}")

#测试cookies
def test_with_cookies():
    url = "https://httpbin.org/cookies"

    #发送带cookies的请求
    cookies = {"session":"abc123","user":"cg12"}
    response = requests.get(url,cookies=cookies)

    assert response.status_code == 200
    assert response.json()["cookies"]["user"] == "cg12"
    print(f"\nCookies响应：{response.json()['cookies']}")

#测试Session保持登录状态
def test_session_login():
    session = requests.session()

    #第一次请求：模拟登录
    login_url = "https://httpbin.org/cookies/set"
    session.get(login_url,params={"token":"logged_in"})

    #第二次请求：自动携带Cookies
    profile_url = "https://httpbin.org/cookies"
    response = session.get(profile_url)

    assert response.status_code == 200
    assert response.json()["cookies"]["token"] == "logged_in"
    print(f"\nSession Cookie：{response.json()['cookies']}")

#测试重定向
def test_redirect():
    url = "https://httpbin.org/redirect/2"

    #默认跟随重定向
    response = requests.get(url)
    assert response.status_code == 200
    assert response.url == "https://httpbin.org/get"

    #不跟随重定向
    response = requests.get(url,allow_redirects=False)
    assert response.status_code == 302
    print(f"\n重定向测试通过")

#测试响应解析
def test_response_parsing():
    """测试不同响应格式解析"""
    #JSON响应
    json_url = "https://httpbin.org/json"
    response = requests.get(json_url)
    assert response.json() is not None

    #文本响应
    text_url = "https://httpbin.org/html"
    response = requests.get(text_url)
    assert "<html>" in response.text

    #二进制响应
    image_url = "https://httpbin.org/image/png"
    response = requests.get(image_url)
    assert response.content.startswith(b'\x89PNG')

    print("\n响应解析测试通过")