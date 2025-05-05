import requests
import json

url = 'https://ru.yougile.com/api-v2/projects'
headers = {
    "Authorization": "Bearer EXkCw3gPrErql0qZK9T99uUUYaVFjWT5hyIQswH-Q7gVxSiHRQuaSvKok3XKQKYS",
    'Content-Type': 'application/json'
}
data = {
    "title": "Del project",
    "users": {
        "1c95b193-78b2-4095-99af-323c6c730bc0": "worker"
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
