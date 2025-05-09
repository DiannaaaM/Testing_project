import pytest
import requests


@pytest.mark.positive
def test_GET_response():
    id = 'c6011640-857f-4209-a2ab-af21d95fd30c'
    url = f'https://ru.yougile.com/api-v2/projects/{id}'
    token = 'YOUR_TOKEN'
    headers = {
        "Authorization": f"Bearer {token}",
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    assert response.status_code == 200