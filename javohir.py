import requests

url="https://nbu.uz/exchange-rates/json/"
response=requests.get(url)
# print(dir(response))
print(response.status_code)
print(response.json())