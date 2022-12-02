# from pprint import pprint
import io
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from function import get_list

with io.open("phonebook_raw.csv",encoding= 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)


# # TODO 1: выполните пункты 1-3 ДЗ
pattern = re.compile(r'(^[а-яёА-ЯЁ]*)([\s,]*)([а-яёА-ЯЁ]*)([\s,]*)([а-яёА-ЯЁ]*)'
                     r'([\s,]*)([а-яёА-ЯЁ]*)([\s,]*)([а-яёА-ЯЁc\s–]*)([\s,]*)([+7|8]*)([\s)(]*)'
                     r'([0-9]{0,3})([\s)(-]*)([0-9]{0,3})([\s)(-]*)([0-9]{0,2})([\s)(-]*)([0-9]{0,2})([\s)'
                     r'(]*)([доб.]*)([\s]*)([0-9]{0,4})([\s,)(]*)([a-zA-Z.@1-9]*)')
number_circle = 0
contacts = []

for row in contacts_list:
  test = " ".join(row)
  number_circle +=1
  if number_circle == 1:
    pass
  else:
    result = re.match(pattern, test)
    contact = {'lastname': result[5], 'firstname': result[3], 'surname': result[1],'organization': result[7],
      'position': result[9], 'phone': f'+7-{result[13]}-{result[15]}-{result[17]}-{result[19]} {result[21]}{result[23]}','email': result[25]}
    contacts.append(contact)

finish_list = get_list(contacts)


# # TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
fields = ['lastname','firstname','surname','organization','position','phone','email']
with open("phonebook.csv", "w") as f:
  datawriter = csv.DictWriter(f, fields,extrasaction='ignore')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(finish_list)