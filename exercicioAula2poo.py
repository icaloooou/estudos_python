## exercicio 1
#foi pedido que preenchessemos uma lista com 10 números digitados pelo usuário, depois para mostrassemos o maior e o menor número da lista,
#a quantidade de números pares, a média dos números contidos na lista e todos os números menores que o valor da média calculada.

listaUsuario = []
for i in range(10):
    n = int(input('número: '))
    listaUsuario.append(n)

print('maior: ', max(listaUsuario))
print('menor :', min(listaUsuario))

contarPares = 0
for a in listaUsuario:
    if a % 2 == 0:
        contarPares += 1
print('numeros pares :', contarPares)

media = sum(listaUsuario) / len(listaUsuario)
print('média : ', media)

for b in listaUsuario:
    if b < media:
        print('numero menor que a media :', b)


## exercicio 2
#nesse exercício foi pedido que preenchessemos uma lista com 10 números digitados pelo usuário e a partir dessa lista
#gerassemos uma lista apenas com os números pares e outra apenas com os números impares.

listaUsuario2 = []
for i in range(10):
    n = int(input('número: '))
    listaUsuario2.append(n)
print(listaUsuario2)

listaPar = []
listaImpar= []
for g in listaUsuario2:
    if g % 2 == 0:
        listaPar.append(g)
    else:
        listaImpar.append(g)
print('lista par :', listaPar)
print('lista impar :', listaImpar)


## exercicio 3 - primeira versão
#aqui foi solicitado que criassemos duas tuplas com 5 números digitados pelo usuário e em seguida que fizessemos a concatenação e exibissimos o resultado

def criarTupla():
    return int(input('número tupla: '))

tuplaUser1 = (criarTupla(), criarTupla(), criarTupla(), criarTupla(), criarTupla()) #essa foi a forma não muito funcional que pude criar como primeira versão
tuplaUser2 = (criarTupla(), criarTupla(), criarTupla(), criarTupla(), criarTupla())
print('tupla 1 :', tuplaUser1)
print('tupla 2 :', tuplaUser2)
print('concatenação de tuplas :', tuplaUser1 + tuplaUser2)

##exercicio 3 - segunda versão
def criarListas(t):
    for i in range(3):
        n = int(input('número lista: '))
        t.append(n)

lista1 = []
lista2 = []
primeira = (criarListas(lista1))
segunda = (criarListas(lista2))
tupla1 = tuple(lista1)
tupla2 = tuple(lista2)
print(tupla1)
print(tupla2)

tuplaConcatenada = tupla1 + tupla2
print(tuplaConcatenada)

## exercicio 4 - primeira versão
#deveriamos usar uma função chamada 'intercala_numeros' para que ela pudesse receber duas listas de três itens e retornar uma lista de seis itens, com os números intercalados.

def criarListas(t):
    for i in range(3):
        n = int(input('número lista: '))
        t.append(n)

def intercala_numeros():
    return listaUser1[0], listaUser2[0], listaUser1[1], listaUser2[1], listaUser1[2], listaUser2[2]

listaUser1 = []
listaUser2 = []

primeira = (criarListas(listaUser1))
segunda = (criarListas(listaUser2))
print('lista 1 :', listaUser1)
print('lista 2 :', listaUser2)
print('numeros intecalados das duas listas: ', intercala_numeros())

##exercicio 4 - segunda versão
def criarListas(t):
    for i in range(3):
        n = int(input('número lista: '))
        t.append(n)

def intercalaNumeros2(lista1, lista2):
    lista3 = []
    for i in range(3):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3

listaUser1 = []
listaUser2 = []
primeira = (criarListas(listaUser1))
segunda = (criarListas(listaUser2))
listaIntercalada = intercalaNumeros2(listaUser1, listaUser2)

print('lista 1 :', listaUser1)
print('lista 2 :', listaUser2)
print('numeros intecalados das duas listas: ', listaIntercalada)
