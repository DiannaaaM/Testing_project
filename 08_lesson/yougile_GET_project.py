import requests
import json

id = 'c6011640-857f-4209-a2ab-af21d95fd30c'
url = f'https://ru.yougile.com/api-v2/projects/{id}'
headers = {
    "Authorization": "Bearer EXkCw3gPrErql0qZK9T99uUUYaVFjWT5hyIQswH-Q7gVxSiHRQuaSvKok3XKQKYS",
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())
