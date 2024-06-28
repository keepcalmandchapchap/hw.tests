import pytest

@pytest.mark.parametrize('test_input, expected',
                         [
                             ('folder_1', 201),
                             ('folder_2', 201),
                             pytest.param('folder_1', 201, marks=pytest.mark.xfail)
                         ]
                         )
def test_create_folder_in_yandex_disk(yandex_connect, test_input, expected):
    yandex_connect.create_folder(test_input)
    assert yandex_connect.value_status_code() == expected, f'Folder with name {test_input} has been already created'
    yandex_connect.delete_folder(test_input)
