import unittest
import requests

class TestDeleteCourse(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000/api/courses'
        # 在测试之前添加一些课程数据到数据库，用于后续的删除测试
        self.course_ids = self.add_dummy_courses()

    def tearDown(self):
        # 在测试完成后清理测试数据
        self.delete_dummy_courses()

    def add_dummy_courses(self):
        # 添加一些测试数据到数据库，并返回这些课程的ID
        course_ids = []
        for i in range(1, 6):
            data = {
                'name': f'课程{i}',
                'time': f'周一 10:00-12:00',
                'location': f'教室{i}'
            }
            response = requests.post(self.base_url, json=data)
            self.assertEqual(response.status_code, 200)
            course_id = response.json().get('course_id')
            course_ids.append(course_id)
        return course_ids

    def delete_dummy_courses(self):
        # 删除之前添加的测试数据
        for course_id in self.course_ids:
            response = requests.delete(f'{self.base_url}/{course_id}')
            self.assertEqual(response.status_code, 200)

    def test_delete_single_course(self):
        # 测试删除单个课程
        course_id_to_delete = self.course_ids[0]  # 删除第一个课程
        response = requests.delete(f'{self.base_url}/{course_id_to_delete}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], '授業情報が削除されました。')

        # 确认课程已被删除
        response = requests.get(f'{self.base_url}/{course_id_to_delete}')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], '指定された授業が見つかりません。')

    def test_delete_multiple_courses(self):
        # 测试删除多个课程
        course_ids_to_delete = self.course_ids[1:3]  # 删除第二个和第三个课程
        data = {'courseIds': course_ids_to_delete}
        response = requests.delete(self.base_url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json())
        self.assertEqual(response.json()['message'], '授業情報が削除されました。')

        # 确认课程已被删除
        for course_id in course_ids_to_delete:
            response = requests.get(f'{self.base_url}/{course_id}')
            self.assertEqual(response.status_code, 404)
            self.assertIn('error', response.json())
            self.assertEqual(response.json()['error'], '指定された授業が見つかりません。')

if __name__ == '__main__':
    unittest.main()

