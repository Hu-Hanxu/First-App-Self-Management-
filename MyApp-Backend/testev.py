import requests
from datetime import datetime

url = 'http://192.168.48.140:5000/api/events'
data = {
    'name': 'Event Name',
    'date': datetime(2023, 7, 28).isoformat()  # 将日期转换为 ISO 格式的字符串
}

response = requests.post(url, json=data)

print('POST响应状态码:', response.status_code)
print('POST响应内容:', response.json())
