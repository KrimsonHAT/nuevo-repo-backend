from dogs_description import dogs_list
from dogs_class import Dog   

my_dog_list = []

def add_dog():
    name = input('name: \n')
    breed = input('breed: \n')
    size = input('size: \n')
    color = input('color: \n')
    weight = input('weight: \n')
   

    new_dog = Dog(name,breed,color,size,weight,)
    my_dog_list.append(new_dog)


def show():
    for dog in my_dog_list:
        print(dog)

def menu():
    print(' [i] introducir nuevo registro ')
    print(' [m] mostrar todos los perrunos  ')
    print(' [s] salir ')
    print(' [e] emitir ladrido ')

def make_noise(name):
    for dog in my_dog_list:
       if dog.name == name:
            return dog.bark()
    print ('ups ese perro no existe')
        




while True:
    menu()
    option = input()
    if option == 's':
        print('Bye!!')
        break
    elif option =='i':
        add_dog()
    elif option =='m':
        show()
    elif option =='e':
        name = input('¿como se llama?')
        make_noise (name)
   
    '''
first_dog = Dog(**dog_desription)
first_dog.bark()
first_dog.eat()
'''
