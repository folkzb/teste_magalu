import os
numero='oi'

def isint(num):
        try:
            int(num)
            return True
        except ValueError:
            return False


while numero != 'sair':
    while isint(numero) == False:
        if numero=='sair':
            break
        else:
            numero = input("Digite um número: ")
    if numero =='sair':
        break
    else:
        numero = int(numero)
    if numero < 10:
        print('O número é menor que 10.')
    else:
        pass
    if numero%2 != 1 and numero !=80:
        print('O número é Par.')
    else:
        pass
    if numero%2 != 0 and numero !=51:
        print('O número é Impar.')
    else:
        pass
    if numero < 16 and numero > 8:
        print('O número está entre 8 e 16.')
    else:
        pass
    if numero == 51 or numero == 80:
        print('O número é 51 ou 80.')
    else:
        pass
    if numero == 101:
        print('')
    else:
        pass
    if numero == numero:
        numero=''
    else:
        pass