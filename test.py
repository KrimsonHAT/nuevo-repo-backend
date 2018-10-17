#message = input("introduce un mensaje")
#print("This is the message:" , message)
'''eset es un comentario
de mas de una linea 
waoooooo
'''

'''
number1 =int (input('give me the first number'))
number2 = int (input('give me the second number'))

_sum = number1 + number2

if _sum == 10:
    print('okay u got ten')
elif _sum > 10:
    print ('u got more than ten')
else:
    print('is not ten')
'''


while True:
    try:
        numero1 = int(input('give me some value'))
        numero2 = int(input('give me the second value'))
        _sum = numero1 + numero2
        if _sum == 10:
            print('si es igual a 10')
            break
        elif _sum > 10:
            print('es mayor a 10')
        else:
         print('What =(')
    except ValueError:
        print('Esto esta mal no sumo strings')
        break
