import requests

# 请求的 URL
url = 'http://localhost:5000/api/tests'

# 请求头中的 Content-Type
headers = {'Content-Type': 'application/json'}

# 请求体中的 JSON 数据
data = {
    'time': '1',
    'name': '1',
    'location': '1'
}

# 发送 POST 请求
response = requests.post(url, json=data, headers=headers)

# 输出响应结果
print(response.json())
