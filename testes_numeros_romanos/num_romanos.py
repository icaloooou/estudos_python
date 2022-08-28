

def converte(s):
    dicionario = {
        'I': 1, "V": 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if type(s) != str:
        raise TypeError('Insira um numero romano _nao convertido_')
    else:
        simbolo = s.upper()
    
    if len(simbolo) == 1:
        resultado = dicionario.get(simbolo, 'Tente outro numero romano')
    elif len(simbolo) == 2:
        num_um = dicionario.get(simbolo.strip()[0])
        num_dois = dicionario.get(simbolo.strip()[1])
        if num_um == 1:
            resultado = num_dois - num_um
        else:
            resultado = num_um + num_dois
    else:
        resultado = 'Ainda não implementado, tente numeros apenas com duas casas'

    return resultado
