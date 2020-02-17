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

mil = ['mil']

ddd = '200'

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
        return mil[0]
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
print(numero(1000))