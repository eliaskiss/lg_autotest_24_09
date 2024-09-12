import requests

url = "http://127.0.0.1:5000/rest"

payload = {"params": {
        "command": "sum",
        "a": 10,
        "b": 20
    }}
headers = {
    "Content-Type": "application/json",
    "User-Agent": "insomnia/9.3.2"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)