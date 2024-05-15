import requests

id = 'test'
json_data = {'key': 'value'}
request_post = requests.post(
    url="http://localhost:8000/v1/api/{}".format(id),
    json=json_data
)
print(request_post)
request_get = requests.get(
    url="http://localhost:8000/v1/get/{}".format(id),
)
