import unittest
import requests

class TestGitHubAPI(unittest.TestCase):
    
    def setUp(self):
        """每个测试方法执行前运行，定义基础 URL"""
        self.base_url = "https://api.github.com"
        # 如果你需要认证，可以在这里设置 headers
        # 但 GitHub API 的公开端点无需认证也可以调用
    
    def test_root_returns_200(self):
        """测试 GitHub API 根端点返回状态码 200"""
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200, "根端点应返回 200")
    
    def test_nonexistent_returns_404(self):
        """测试不存在的端点返回状态码 404"""
        url = f"{self.base_url}/non_existent_endpoint_123"
        response = requests.get(url)
        self.assertEqual(response.status_code, 404, "不存在的端点应返回 404")
    
    def test_search_has_items(self):
        """测试搜索 'testing' 关键词，验证返回数据包含 items 字段"""
        search_url = f"{self.base_url}/search/repositories?q=testing"
        response = requests.get(search_url)
        data = response.json()
        self.assertIn("items", data, "搜索结果中应包含 'items' 字段")

if __name__ == "__main__":
    unittest.main(verbosity=2)