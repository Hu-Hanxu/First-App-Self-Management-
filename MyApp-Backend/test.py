import requests

# 定义要删除的事件ID
event_id_to_delete = 1

# 请求的URL
url = f'http://192.168.48.140:5000/api/events/{event_id_to_delete}'

# 发送删除请求
response = requests.delete(url)

# 解析响应
if response.status_code == 200:
    print('删除成功！')
else:
    print(f'删除失败：{response.json()}')
