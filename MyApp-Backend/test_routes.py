import unittest
import requests

class TestAddCourse(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/api/courses'

    def test_add_course(self):
        course_data = {
            'name': 'Math Course',
            'time': '2023-07-30 09:00:00',
            'location': 'Room 101',
        }

        response = requests.post(self.BASE_URL, json=course_data)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertIn('course_id', data)

        course_id = data['course_id']
        self.assertIsInstance(course_id, int)

    def test_add_course_missing_data(self):
        course_data = {
            'name': 'Math Course',
            # 'time': '2023-07-30 09:00:00',  # 缺少必要的时间字段
            'location': 'Room 101',
        }

        response = requests.post(self.BASE_URL, json=course_data)
        data = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

class TestDeleteCourse(unittest.TestCase):
    BASE_URL = 'http://localhost:5000/api/courses'

    def test_delete_course(self):
        # 首先添加一个课程，然后测试删除该课程
        course_data = {
            'name': 'Math Course',
            'time': '2023-07-30 09:00:00',
            'location': 'Room 101',
        }

        response = requests.post(self.BASE_URL, json=course_data)
        data = response.json()
        course_id = data['course_id']

        delete_response = requests.delete(f'{self.BASE_URL}/{course_id}')
        delete_data = delete_response.json()

        self.assertEqual(delete_response.status_code, 200)
        self.assertIn('message', delete_data)

if __name__ == '__main__':
    unittest.main()

