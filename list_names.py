documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

command = input('Введите команду ln: ')

def list_name():
  """
  list all documents name
  """
   for document in documents:
    try:
      print(document['name'])
    except KeyError:
      print('У документа {} нет ключа name'.format(document))

if command.lower() == 'ln':
  list_name()
else:
  print('Неверная команда')
