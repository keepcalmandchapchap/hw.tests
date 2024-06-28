from src.task_1.secretary import get_directory, get_name, add
import pytest

@pytest.mark.parametrize('test_input, expected', 
                            [
                                ('10006', 'Аристарх Павлов'),
                                ('11-2', 'Геннадий Покемонов'),
                                pytest.param('101', 'Джордж Буш', marks=pytest.mark.xfail)
                            ]
                        )
def test_get_name(get_documents, test_input, expected):
    result = get_name(documents=get_documents, doc_number=test_input)
    assert result == expected, 'Result is not equal to the expected value'



@pytest.mark.parametrize('test_input, expected', 
                            [
                                ('11-2', '1'),
                                ('10006', '2'),
                                pytest.param('2207 876234', '3', marks=pytest.mark.xfail)
                            ]
                        )
def test_get_directory(get_directories, test_input, expected):
    result = get_directory(directories=get_directories, doc_number=test_input)
    assert result == expected, 'Result is not equal to the expected value'


@pytest.mark.parametrize('test_input, expected',
                            [
                                (('international passport', '311 020203', 'Александр Пушкин', 3), True),
                                (('passport', '123-456', 'Дмитрий Лазарев', 2), True),
                                pytest.param(('driver licencse', '322', 'Владимир Центральный', 4), True, marks=pytest.mark.xfail)
                            ]
                         )
def test_add(get_directories, get_documents, test_input, expected):
    docs = get_documents
    direct = get_directories
    result = False
    add(*test_input, directories=direct, documents=docs)
    for person in docs:
        if list(test_input[:3]) == list(person.values()):
            result = True
    assert result == expected, 'Person was not added to the documents dictionary'
    

