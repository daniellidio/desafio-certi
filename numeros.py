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
            if str(num)[1:2] == '1':
                return um_a_dezenove[num // 1000] + ' mil e cem'
            else:
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
        elif str(num)[2:5] == '000': #xx000
            if int(str(num)[:2]) < 20:
                return um_a_dezenove[num // 1000] + ' mil'
            else:
                return dezenas[(int(str(num)[0:2])) // 10 - 1] + ' e ' + um_a_dezenove[(int(str(num)[0:2])) % 10] + ' mil'
        elif str(num)[1:2] == '0' and str(num)[3:5] == '00': #x0x00
            if str(num)[2:3] == '1':
                return dezenas[int(str(num)[:1]) // 10000] + ' mil e cem'
            else:
                return dezenas[int(str(num)[:1]) // 10000] + ' mil e ' + centenas[int(str(num)[2:3]) - 1]
        elif str(num)[1:3] == '00' and str(num)[4:5] == '0': #x00x0
            return dezenas[num // 10000 - 1] + ' mil e ' + dezenas[int(str(num)[3:4]) - 1]
        elif str(num)[1:4] == '000': #x000x
            return dezenas[num // 10000 - 1] + ' mil e ' + um_a_dezenove[int(str(num)[4:5])]
        elif str(num)[3:5] == '00': #xxx00
            if int(str(num)[0:2]) < 20 and str(num)[2:3] == '1':
                return um_a_dezenove[int(str(num)[0:2])] + ' mil e cem'
            elif int(str(num)[0:2]) < 20 and str(num)[2:3] != '1':
                return um_a_dezenove[int(str(num)[0:2])] + ' mil e ' + centenas[int(str(num)[2:3]) - 1]
            elif int(str(num)[0:2]) >= 20 and str(num)[2:3] == '1':
                return dezenas[int(str(num)[:1])] + ' e ' + um_a_dezenove[int(str(num)[1:2])] + ' mil e cem'
            elif int(str(num)[0:2]) >= 20 and str(num)[2:3] != '1':
                return dezenas[int(str(num)[:1])] + ' e ' + um_a_dezenove[int(str(num)[1:2])] + ' mil e' + \
                    centenas[int(str(num)[2:3])]
    else:
        return 'Escreva um número de 0 a 9999'

print(numero(20050))
print(numero(12000))
print(numero(19000))
print(numero(92000))
print(numero(19100))
print(numero(19200))

print('12345'[0:2])