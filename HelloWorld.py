import os

def comprimento(**kwargs):
    if 'geek' in kwargs and kwargs['geek']=='Victor':
        return'Você é pythonico'
    elif 'geek' in kwargs:
        return 'Geek'
    return 'Não tenho certeza de quem você é'    


print(comprimento(geek='Victor'))

def parametros(num1,num2,*args,seila=True,**kwargs):
    print(num1,num2,args,seila,kwargs)


parametros(1,2,3,4,5,6,seila=False,nome='Victor',sobrenome='Alexandre')

lista=[1,2,3,4,5,6]

def func(valor: int)-> int:
    return valor * 2

lista2 = [func(x) for x in lista]
print(lista2)

print([valor*2 for valor in range(1,5)])    

print([valor for valor in range(1,11) if valor % 2 != 0])

nome_completo = lambda nome, sobrenome : nome.strip().title() + ' ' + sobrenome.strip().title() 
print(nome_completo('victor       ','         alexandre'))

raios = [2,3,4,5,6,7]

print(list(map(lambda r:(r**2)*3.14,raios)))

temp = [('São Paulo',22),('Parana',18),('Minas Gerais',25)]

c_para_f = lambda dado:(dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f,temp)))

maiores = lambda valor : valor > 3
print(list(filter(maiores,raios)))


valores = [" ","a"," ","b"," "," ","c"]
filtro = lambda valor: valor != " "
print(list(filter(filtro,valores)))

nomes = ['Victor','Xispita','Nenem','Fifi']
mapa=lambda nome:f'Meu nome e {nome}'
filtro = lambda nome:len(nome)>5
print(list(map(mapa,filter(filtro,nomes))))
res = list(filter(filtro,nomes))
res = list(map(mapa,res))
print(res)


from functools import reduce

numeros = list(range(1,11,1))
acum = lambda x,y:x+y
print(reduce(acum,numeros))

nomes = ['José','Jaqueline','Joana','Joao','Jaspion']
print(all([nome[0] == 'J' for nome in nomes]))

print(all([letra for letra in 'eio' if letra in 'aeiou']))

pares = [valor for valor in range(1,21) if valor % 2 ==0]
print(list(pares))

print(all([valor==1 for valor in range(1,21) if valor % 2 == 0]))

produtos = [
    {'nome':'notebook' , 'preco':4500},
    {'nome':'smartphone' , 'preco':2800},
    {'nome':'impressora' , 'preco':1300},
    {'nome':'mouse' , 'preco':132},
]

def prod_caros(p):
    return p['preco']>2000
caros=filter(prod_caros,produtos)
for i in caros:
    print (i)


print(sorted(produtos,key=lambda produto:produto['preco']))



clientes = {
    'cliente1':{
        'nome':"Victor",
        'valor':1
    },
    'cliente2':{
        'nome':'Xispita',
        'valor':2
    }
}

for chave,valor in clientes.items():
    print(f'{chave}')
    for k,v in valor.items():
        print(f'\t{k} {v}')


import copy

dic = copy.deepcopy(clientes)
print(dic)

lista = [1,2,3,4,5,6,7,8,9]
print(lista[:-1])

ex = [(x,y) for x in lista for y in range(3)]
print(ex)

nomes = ['Victor','Xispita','Nenem','Fifi','Peta','Banca','Negona','Neguinha']
print([nome.replace('a','@') for nome in nomes])


from collections import deque

fila = (['A','B','C'])

fila.append('D')

print(fila)



print(fila)

tupla = (
    ('chave','valor'),
    ('chave2','valor2')
)

ex5 = [(y,x) for x,y in tupla]
print(ex5)

l3 = list(range(100))
ex6 = [v if v % 2 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex6)

ex7 = [v for v in l3 if v % 2 == 0]
print(ex7)

ex8 = {c : v for c , v in tupla}
print(ex8)

print({c:v**2 for c,v in enumerate(range(10))})

import time
import sys
gerador = (x for x in range(1000))
print(f'Tamanho do gerador {sys.getsizeof(gerador)}')

for valor in gerador:
    print(valor)

















































































