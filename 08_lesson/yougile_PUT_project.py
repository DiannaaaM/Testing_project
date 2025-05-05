import requests
import json

id = 'c6011640-857f-4209-a2ab-af21d95fd30c'
url = f'https://ru.yougile.com/api-v2/projects/{id}'
headers = {
    "Authorization": "Bearer EXkCw3gPrErql0qZK9T99uUUYaVFjWT5hyIQswH-Q7gVxSiHRQuaSvKok3XKQKYS",
    'Content-Type': 'application/json'
}
data = {
    "deleted": True,
    "title": "Del project",
    "users": {
        "1c95b193-78b2-4095-99af-323c6c730bc0": "worker"
    }
}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
