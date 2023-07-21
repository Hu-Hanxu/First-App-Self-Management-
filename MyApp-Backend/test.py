import requests

# 请求的 URL
url = 'http://localhost:5000/api/courses'

# 请求头中的 Content-Type
headers = {'Content-Type': 'application/json'}

# 请求体中的 JSON 数据
data = {
    'name': '计算机科学',
    'time': '周一 10:00-12:00',
    'location': ''
}

# 发送 POST 请求
response = requests.post(url, json=data, headers=headers)

# 输出响应结果
print(response.json())
