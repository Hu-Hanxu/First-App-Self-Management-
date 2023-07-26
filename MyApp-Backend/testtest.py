# testtest.py

import unittest
import requests

class TestAddTest(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/api/tests'

    def test_add_test(self):
        # 正确的测试数据
        test_data = {
            'name': 'Math Exam',
            'time': '2023-07-30 09:00:00',
            'location': 'Room 101',
        }

        response = requests.post(self.BASE_URL, json=test_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertIn('test_id', response.json())

        test_id = response.json()['test_id']
        self.assertIsInstance(test_id, int)

    def test_add_test_missing_data(self):
        # 缺少必要的测试数据
        test_data = {
            'name': 'Math Exam',
            'time': '2023-07-30 09:00:00',
            # 'location': 'Room 101',  # 这里故意省略了地点字段
        }

        response = requests.post(self.BASE_URL, json=test_data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_add_test_database_error(self):
        # 模拟数据库连接失败
        test_data = {
            'name': 'Math Exam',
            'time': '2023-07-30 09:00:00',
            'location': 'Room 101',
        }

        response = requests.post(self.BASE_URL, json=test_data)

        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()
