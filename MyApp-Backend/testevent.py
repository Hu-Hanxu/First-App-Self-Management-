import requests

def test_delete_event(event_id):
    # 发起DELETE请求，删除指定ID的事项
    url = f'http://172.25.3.19:5000/api/events/{event_id}'
    response = requests.delete(url)

    # 解析响应数据
    try:
        data = response.json()
        print('DELETE响应状态码:', response.status_code)
        print('DELETE响应内容:', data)
        # 验证删除是否成功（可根据实际返回的JSON格式进行验证）
        assert response.status_code == 200
        assert 'message' in data and data['message'] == 'イベント削除成功！'
        print(f'测试删除事项成功！事项ID: {event_id}')
    except requests.exceptions.JSONDecodeError as e:
        print('DELETE响应内容解析失败:', e)
    except AssertionError:
        print(f'测试删除事项失败！事项ID: {event_id}')



if __name__ == '__main__':
    # 假设要删除的事项ID为1，您可以根据实际情况修改为其他存在的事项ID
    test_delete_event(1)
