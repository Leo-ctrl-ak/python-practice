import requests
import os
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
url = "https://api.github.com"
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

response = requests.get(url, headers=headers)

print(f"状态码: {response.status_code}")
print("响应内容:")
print(response.text)