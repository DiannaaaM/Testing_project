import requests
import pytest


@pytest.mark.support
def test_PUT_request():
    id = 'c6011640-857f-4209-a2ab-af21d95fd30c'
    url = f'https://ru.yougile.com/api-v2/projects/{id}'
    token = 'YOUR_TOKEN'
    headers = {
        "Authorization": f"Bearer {token}",
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
    assert response.status_code == 200



@pytest.mark.xfail(reason='Намеренный провал')
def test_PUT_request_fail():
    id = 'c6011640-857f-4209-a2ab-af21d95fd30c'
    url = f'https://ru.yougile.com/api-v2/projects/{id}'
    token = 'YOUR_TOKEN'
    headers = {
        "Authorization": f"Bearer {token}",
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
    assert response.status_code == 200