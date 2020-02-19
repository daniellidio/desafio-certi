um_a_dezenove = [
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'
]

dezenas = [
    'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
    'setenta','oitenta', 'noventa'
]

centenas = [
    'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
    'seiscentos', 'setecentos', 'oitocentos', 'novecentos'
]

def numero(num):
    if num < 20:
        return um_a_dezenove[num]
    elif num >= 20 and num <= 99:
        if str(num)[1:2] == '0':
            return dezenas[num // 10 - 1]
        else:
            return dezenas[num // 10 - 1] + ' e ' + um_a_dezenove[num % 10]
    elif num == 100:
        return 'cem'
    elif num > 100 and num <= 999:
        if str(num)[1:3] == '00':
            return centenas[num // 100 - 1]
        elif str(num)[2:3] == '0':
            return centenas[num // 100 - 1] + ' e ' + dezenas[(num - (int(str(num)[:1]) * 100)) // 10 - 1]
        else:
            return centenas[num // 100 - 1] + ' e ' + dezenas[(num - (int(str(num)[:1]) * 100)) // 10 - 1] + \
            ' e ' + um_a_dezenove[num - ((int(str(num)[:2])) * 10)]
    elif num == 1000:
        return 'mil'
    elif num < 10000:
        if str(num)[1:4] == '000': #x000
            return um_a_dezenove[num // 1000] + ' mil'
        elif str(num)[2:4] == '00': #xx00
            return um_a_dezenove[num // 1000] + ' mil e ' + centenas[(num - (int(str(num)[:1]) * 1000)) // 100 - 1]
        elif str(num)[1:2] == '0' and str(num)[2:3] != '0' and str(num)[3:4] == '0': #x0x0
            return um_a_dezenove[num // 1000] + ' mil e ' + dezenas[(num - (int(str(num)[:1]) * 1000)) // 10 - 1]
        elif str(num)[1:3] == '00': #x00x
            return um_a_dezenove[num // 1000] + ' mil e ' + um_a_dezenove[(num - (int(str(num)[:1]) * 1000))]
        elif str(num)[3:4] == '0': #xxx0
            return um_a_dezenove[num // 1000] + ' mil e ' + centenas[(num - (int(str(num)[:1]) * 1000)) // 100 - 1] + \
                ' e ' + dezenas[(int(str(num)[2:4])) // 10 - 1]
        elif str(num)[1:2] == '0': #x0xx
            if int(str(num)[2:4]) < 20:
                return um_a_dezenove[num // 1000] + ' mil e ' + um_a_dezenove[(num - (int(str(num)[:1]) * 1000))]
            else:
                return um_a_dezenove[num // 1000] + ' mil e ' + dezenas[(num - (int(str(num)[:1]) * 1000)) // 10 - 1] + \
                    ' e ' + um_a_dezenove[(int(str(num)[3:4]))]
        else:
            return um_a_dezenove[num // 1000] + ' mil e ' + centenas[(num - (int(str(num)[:1]) * 1000)) // 100 - 1] + \
                ' e ' + dezenas[(int(str(num)[2:4])) // 10 - 1] + ' e ' + um_a_dezenove[int(str(num)[3:4])]
    elif num < 100000:
        if str(num)[1:5] == '0000': #x0000:
            return dezenas[num // 10000 - 1] + ' mil'
        #elif str(num)[2:5] == '000': #xx000
        #    return 
    else:
        return 'Escreva um número de 0 a 9999'

'''
print(numero(0))
print(numero(2))
print(numero(11))
print(numero(99))
print(numero(100))
print(numero(200))
print(numero(220))
print(numero(221))
print(numero(999))
print(numero(1020))
print(numero(2040))
print(numero(2000))
print(numero(2200))
print(numero(2001))
print(numero(2210))
print(numero(2011))
print(numero(2020))
print(numero(2021))
print(numero(2021))
print(numero(9999))
print(numero(1999))
print(numero(10000))
'''