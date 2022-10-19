import requests
import json
# json.loads(json_data) -> dict

url = "https://api.wiliot.com/v1/auth/token"

querystring = {"username":"connoralydon.biz@gmail.com","password":"WiliotPassword1!"}

headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)

def get_auth():
    pass
    
def get_refresh_auth():
    pass