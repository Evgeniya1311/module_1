#рейтинг на КП
my_dict = {'Interstellar': 8.7, 'The Martian': 7.8, 'Oblivion': 7.2, 'Shutter Island': 8.5}
print(my_dict) #вывод словаря
print(my_dict['Oblivion']) #вывод значения по ключу
print(my_dict.get('Mamba')) #вывод значения по несущ. ключу без ошибки
my_dict.update({'Oppenheimer': 8.1, 'Passengers': 7.2}) #доб. двух пар в словарь
a = my_dict.pop('The Martian')  #удаление пары с возвр. значения
print(a) #вывод значение удаленной пары
print(my_dict) #вывод словаря

my_set = {1, 'a', 'str', True, 1, 4, 1, 'a'}
print(my_set) #вывод мн-ва
my_set.add(7) #добавление эл-та
my_set.add('b') #добавление эл-та
my_set.remove(1) #удаление эл-та
print(my_set) #вывод мн-ва