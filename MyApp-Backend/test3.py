import requests
import json

def test_add_event_success():
    # 发送正确的事件数据
    data = {
        "name": "测试事件",
        "date": "2023-07-31"  # 替换为你希望的事件日期
    }
    response = requests.post('http://127.0.0.1:5000/api/events', json=data)

    if response.status_code == 200:
        response_data = response.json()
        print("测试通过：", response_data)
    else:
        print("测试失败：", response.status_code, response.text)

if __name__ == '__main__':
    test_add_event_success()
