import unittest
import requests

class TestAddSubject(unittest.TestCase):
    def setUp(self):
        # 在测试之前添加测试所需的课程记录
        self.add_dummy_subject()

    def tearDown(self):
        # 在测试之后删除测试添加的课程记录
        self.delete_dummy_subject()

    def add_dummy_subject(self):
        # 请求的 URL
        url = 'http://localhost:5000/api/subjects'

        # 请求头中的 Content-Type
        headers = {'Content-Type': 'application/json'}

        # 请求体中的 JSON 数据
        data = {
            'name': '测试科目',
            'deadline': '2023-07-31',
        }

        # 发送 POST 请求
        response = requests.post(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('subject_id', response.json())

    def delete_dummy_subject(self):
        # 请求的 URL
        url = 'http://localhost:5000/api/courses'

        # 请求头中的 Content-Type
        headers = {'Content-Type': 'application/json'}

        # 请求体中的 JSON 数据
        data = {
            'courseIds': [1],  # 根据测试需要指定要删除的科目ID
        }

        # 发送 DELETE 请求
        response = requests.delete(url, json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_add_subject(self):
        # 请求的 URL
        url = 'http://localhost:5000/api/subjects'

        # 请求头中的 Content-Type
        headers = {'Content-Type': 'application/json'}

        # 请求体中的 JSON 数据
        data = {
            'name': '测试科目',
            'deadline': '2023-07-31',
        }

        # 发送 POST 请求
        response = requests.post(url, json=data, headers=headers)

        # 验证是否成功添加科目
        self.assertEqual(response.status_code, 200)
        self.assertIn('subject_id', response.json())

    def test_add_subject_failure(self):
        # 请求的 URL
        url = 'http://localhost:5000/api/subjects'

        # 请求头中的 Content-Type
        headers = {'Content-Type': 'application/json'}

        # 请求体中的 JSON 数据（不包含必要的字段）
        data = {
            'name': '测试科目',
            # 缺少 deadline 字段
        }

        # 发送 POST 请求
        response = requests.post(url, json=data, headers=headers)

        # 验证是否添加科目失败，期望返回状态码为 400
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

if __name__ == '__main__':
    unittest.main()
