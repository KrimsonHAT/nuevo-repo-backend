#palabra clave para definir funciones 
def print_values(dictionary):
    for key in dictionary:
        print(key,dictionary[key])


my_first_dictionary = {
    'name': 'Panfilo',
    'last_name': 'Membrillo',
    'age':'gg',
    'phone': 1332454665,
    'books': ['Math', 'Arts'],
    'adress':{
        'street': 'menjurie',
        'number': 999
    }
}
print_values(my_first_dictionary)