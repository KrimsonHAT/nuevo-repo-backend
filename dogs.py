from dog_description import dogs_list

from dog_class import Dog
my_dog_list = []
for description in dog_description:
    new_dog = Dog(**description)
    my_dog_list.append(new_dog)



    print("=========================================")

for dog in my_dog_list:
    print(dog.weight)

    '''
first_dog = Dog(**dog_desription)
first_dog.bark()
first_dog.eat()
'''