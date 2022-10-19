import requests

url = "https://api.wiliot.com/v1/auth/token"

querystring = {"username":"connoralydon.biz@gmail.com","password":"WiliotPassword1!"}

headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)