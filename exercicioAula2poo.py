## exercicio 1
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


## exercicio 3
def criarTupla():
    return int(input('número tupla: '))

tuplaUser1 = (criarTupla(), criarTupla(), criarTupla(), criarTupla(), criarTupla(),)
tuplaUser2 = (criarTupla(), criarTupla(), criarTupla(), criarTupla(), criarTupla(),)
print('tupla 1 :', tuplaUser1)
print('tupla 2 :', tuplaUser2)
print('concatenação de tuplas :', tuplaUser1 + tuplaUser2)


## exercicio 4
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
