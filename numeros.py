um_a_dezenove = [
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'
]

dezenas = [
    'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta',
    'setenta','oitenta', 'noventa'
]

centenas = [
    'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
    'seiscentos', 'setecentos', 'oitocentos', 'novecentos'
]

cem = ['cem']

def numero(num):
    if num < 20:
        return um_a_dezenove[num]
    elif num >= 20 and num <= 99:
        return dezenas[num // 10 - 2] + ' e ' + um_a_dezenove[num % 10]
    elif num == 100:
        return cem[0]
    elif num > 100 and num <= 999:
        if str(num)[1:3] == '00':
            return centenas[num // 100 - 1]
        elif str(num)[2:3] == '0':
            return centenas[num // 100 - 1] + ' e ' + dezenas[(num - (int(str(num)[:1]) * 100)) // 10 - 2]
        else:
            return centenas[num // 100 - 1] + ' e ' + dezenas[(num - (int(str(num)[:1]) * 100)) // 10 - 2] + \
            ' e ' + um_a_dezenove[num - ((int(str(num)[:2])) * 10)]
    elif num == 1000:
        return 'mil'
    elif num < 100000:
        if len(str(num)) == 4 and str(num)[1:4] == '000':
            return um_a_dezenove[num // 1000] + ' mil'
        elif len(str(num)) == 4 and str(num)[2:4] == '00':
            return um_a_dezenove[num // 1000] + ' mil e ' + centenas[(num - (int(str(num)[:1]) * 1000)) // 100 - 1]
        elif len(str(num)) == 4 and str(num)[1:2] == '0' and str(num)[2:3] != '0' and str(num)[3:4] == '0':
            return um_a_dezenove[num // 1000] + ' mil e ' + dezenas[(num - (int(str(num)[:1]) * 1000)) // 10 - 2]
        elif len(str(num)) == 4 and str(num)[1:3] == '00':
            return um_a_dezenove[num // 1000] + ' mil e ' + um_a_dezenove[(num - (int(str(num)[:1]) * 1000))]
    else:
        return 'Escreva um número de 0 a 1000'

print(numero(0))
print(numero(2))
print(numero(42))
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
print('1235'[1:2])
print('1235'[2:3])
print('1235'[3:4])
print('1235'[2:4])