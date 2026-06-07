import requests
import json

# 目标 API（免费测试用）
url = "https://jsonplaceholder.typicode.com/posts"

# 要发送的数据
data = {
    "title": "软件测试学习笔记",
    "body": "今天学习了接口测试的 POST 请求，使用 Python requests 库发送数据并验证返回结果。",
    "userId": 1
}

# 发送 POST 请求
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)

# 打印结果
print(f"状态码：{response.status_code}")
print(f"响应头 Content-Type：{response.headers.get('Content-Type')}")
print(f"\n返回数据：")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# 断言验证
assert response.status_code == 201, f"预期 201，实际 {response.status_code}"
data_response = response.json()
assert data_response["title"] == data["title"], "返回的 title 不匹配"
assert "id" in data_response, "返回数据中没有 id 字段"
print(f"\n✅ 测试通过：POST 请求成功，创建的资源 ID 为 {data_response['id']}")