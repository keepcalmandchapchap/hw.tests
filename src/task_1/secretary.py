documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(documents, doc_number):
    result = 'Документ не найден'
    for info in documents:
        if str(doc_number) in info['number']:
            result = info['name']
    return result



def get_directory(directories, doc_number):
    result = 'Полки с таким документом не найдено'
    for index, shelf in directories.items():
        if doc_number in shelf:
            result = index
    return result

def add(document_type, number, name, shelf_number, documents=None, directories=None):
    new_document = {}
    new_document['type'] = document_type
    new_document['number'] = str(number)
    new_document['name'] = name
    documents.append(new_document)
    key = str(shelf_number)
    new_shelf = []
    if key in directories:
        new_shelf.append(str(number))
        directories[key] = new_shelf
    else:
        directories[key].append(str(number))
    
    

# if __name__ == '__main__':
#     print(get_name("10006"))
#     print(get_directory("11-2"))
#     print(get_name("101"))
#     add('international passport', '311 020203', 'Александр Пушкин', 3)
#     print(get_directory("311 020203"))
#     print(get_name("311 020203"))
#     print(get_directory("311 020204"))