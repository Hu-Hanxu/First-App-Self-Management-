import requests
import json

def test_post_course():
    url = 'http://192.168.3.10:5000/api/courses'  # 替换成你的服务器地址

    # 替换成你要测试的课程数据
    course_data = {
        'name': '测试课程',
        'time': '测试时间',
        'location': '测试地点'
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(course_data), headers=headers)

    # 解析响应内容
    response_data = response.json()

    if response.status_code == 200:
        # 请求成功
        print('Success:', response_data.get('message'))
        print('New course ID:', response_data.get('course_id'))
    else:
        # 请求失败
        print('Error:', response_data.get('error'))

if __name__ == '__main__':
    test_post_course()
