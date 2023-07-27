import requests

url = 'http://172.25.3.49:5000/api/markings'
data = [
    {'target': 'Target1', 'marking_check': True},
]

response = requests.post(url, json=data)

print('POST响应状态码:', response.status_code)
print('POST响应内容:', response.text)

# import requests

# url = 'http://172.25.3.49:5000/api/markings'
# data = [
#     {'id': 3, 'target': 'Target3', 'marking_check': True},
#     {'id': 4, 'target': 'Target4', 'marking_check': False},
#     # 可以继续添加更多要更新的数据
# ]

# response = requests.post(url, json=data)

# print('PUT响应状态码:', response.status_code)
# print('PUT响应内容:', response.text)
