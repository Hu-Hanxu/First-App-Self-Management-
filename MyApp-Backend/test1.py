import requests
import json

def test_add_event():
    # 准备测试数据
    event_data = {
        'name': '测试事项',
        'time': '2023-07-26 15:00:00'
    }

    # 发起POST请求，添加事项
    response = requests.post('http://172.25.3.19:5000/api/events', json=event_data)

    # 解析响应数据
    try:
        data = response.json()
        print('POST响应状态码:', response.status_code)
        print('POST响应内容:', json.dumps(data, ensure_ascii=False, indent=2))
        # 验证添加是否成功（可根据实际返回的JSON格式进行验证）
        assert response.status_code == 200
        assert 'message' in data and 'event_id' in data
        print('测试添加事项成功！事项ID:', data['event_id'])
    except requests.exceptions.JSONDecodeError as e:
        print('POST响应内容解析失败:', e)
    except AssertionError:
        print('测试添加事项失败！')

if __name__ == '__main__':
    test_add_event()
