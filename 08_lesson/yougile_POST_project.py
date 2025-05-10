import requests
import pytest

@pytest.mark.positive
def test_POST_request():
    url = 'https://ru.yougile.com/api-v2/projects'
    token = 'YOUR_TOKEN'
    headers = {
        "Authorization": f"Bearer {token}",
        'Content-Type': 'application/json'
    }
    data = {
        "title": "Del project",
        "users": {
            "1c95b193-78b2-4095-99af-323c6c730bc0": "worker"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201


@pytest.mark.xfail(reason='Намеренный провал')
def test_POST_request_fail():
    url = 'https://ru.yougile.com/api-v2/projects'
    token = 'YOUR_TOKEN'
    headers = {
        "Authorization": f"Bearer {token}",
        'Content-Type': 'application/json'
    }
    data = {
        "title": "Del project",
        "users": {
            "1c95b193-78b2-4095-99af-323c6c730bc0": "worker"
        }
    }

    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200