import pytest
import json
from src.task_2.yandex_task import YandexConnect

@pytest.fixture
def yandex_connect():
    with open(r'config\token_yandex.json', encoding='utf-8') as f:
        file_json = json.load(f)

    token = file_json['token']
    return YandexConnect(token)
    