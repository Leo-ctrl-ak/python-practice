import requests
import os

# 从环境变量获取 Token（关键！不要写死 Token）
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# 搜索关键词，例如 "python"
query = "python"
url = f"https://api.github.com/search/repositories?q={query}"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    items = data.get("items", [])[:3]
    print(f"搜索 '{query}' 的前3个仓库：")
    for idx, repo in enumerate(items, 1):
        name = repo.get('full_name')
        stars = repo.get('stargazers_count')
        print(f"{idx}. {name} (⭐{stars})")
else:
    print("请求失败，状态码:", response.status_code)
    print("响应内容:", response.text)