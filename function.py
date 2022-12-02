

def get_list(list_object):
    '''function for clear contact list'''
    # Получили список фамилий без повторений
    surname_list = []
    for i in list_object:
        surname = i.get('surname')
        surname_list.append(surname)
    surname_list = set(surname_list)
    surname_list = list(surname_list)
    # print(surname_list)

    # Отредактированный список и оставшиеся записи
    new_list = []
    list_change = []
    surname_list2 = surname_list.copy()
    for i in list_object:
        surname = i.get('surname')
        if surname in surname_list2:
            surname_list2.remove(surname)
            new_list.append(i)
        else:
            list_change.append(i)

    finish_list = []

    j, k = list_change

    for i in new_list:
        surname = i.get('surname')
        if surname == k.get('surname'):
            i['email'] = k['email']
            finish_list.append(i)
        elif surname == j.get('surname'):
            i['position'] = j['position']
            finish_list.append(i)
        else:
            finish_list.append(i)
    return(finish_list)