'''
fabricaremos una calculadora minimalista...
las unicas opercaiones disponibles seria suma y resta


empezara pidiendo un nùmero seguido del signo ("+", "-") y despues el segundo, finalizando
'''
result = 0
try:
    while True:
        value_1 = input('Dame el primer valor') if result == 0 else result
        if value_1 == 'salir':
            break
        value_1 = int(value_1)

        sign = input('dame el signo') #should be + or -
        if sign =='salir':
            break

        value_2 = input('Dame el segundo valor')
        
        if value_2 == 'salir':
            break

        value_2 = int(value_2)

        if sign == '+':
            result = value_1 + value_2
        elif sign == '-':
            result = value_1 - value_2
        else:
            raise ValueError('error al insertar el signo, bye')
        print(result)

except ValueError as error:
    print('ups', error)


        