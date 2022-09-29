from itertools import count


lista = list(range(1,100))

ex1 = [v if v % 2 == 0 else 0 for v in lista]
print(ex1)

ex2 = [ v if v % 2 == 0 and v % 3 == 0 else 0 for v in lista]
print(ex2)

from itertools import count
from time import sleep

contador = count(start=1,step=1)
for valor in contador:
    sleep(0.1)
    print(valor)
    if valor == 10:
        break

def func(*args, **kwargs):
    print(args)
    print(kwargs)
    nome = kwargs.get('nome')

    if nome is not None:
        print(nome)

func(nome='Victor')
lista=[1,2,3,4,5,6]
func(*lista)


lista= [
    ['p1',4],
    ['p2',10],
    ['p3',1]
]
print(sorted(lista,key=lambda p:p[1]))

lista.sort(key=lambda p:p[1])
print(lista)
  
dicionario = {'produto1':'camisa'}
dicionario['produto2']='bermuda'
dicionario.update({'produto3':'calça'})
print(dicionario)

if 'produto1' in dicionario.keys():
    print('O produto está no dicionario')

print(dicionario.get('produto3'))

for chave in dicionario.keys():
    print(chave)

for valor in dicionario.values():
    print(valor)

for chave, valor in dicionario.items():
    print(chave,valor)

v = dicionario.copy()
import copy

v1 = copy.deepcopy(v)
print(v1)


import time
def gera():
    for i in range(30):
        yield i
        time.sleep(0.1)

g = gera()

for valor in g:
    print(valor)


seila = ['a','b','c','d','e']
from itertools import count
contador = count()
bla=zip(contador,seila)
for i in bla:
    print(i)

pessoas = [
    {'produto':'p1','preco':12},
    {'produto':'p2','preco':30},
    {'produto':'p3','preco':49},
    {'produto':'p4','preco':2},
    {'produto':'p5','preco':89},
]

filtrados = filter(lambda x:x['preco']>40,pessoas)
for i in filtrados:
    print(i)

lista2=[1,2,3,4,5,6]
nova_lista = map(lambda valor:valor*2,lista2)
print(list(nova_lista))

def converte(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor=float(valor)
            return valor
        except ValueError:
            pass

numero = converte(input('Digite um numero'))
print(numero)


