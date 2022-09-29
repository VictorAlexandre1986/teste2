import copy

d1 = {'chave1':'valor1','chave2':'valor2'}

d2 = copy.deepcopy(d1)

print(d2)

if 'chave3' not in d1:
    d1['chave3'] = 'valor3'

print(d1)

if d1.get('chave1') is not None:
    d1.update({'chave4':'valor4'})

print(d1)

del d1['chave1']

print(d1)

lista = list(range(100))
ex=[valor for valor in lista if valor % 2 == 0 if valor % 4 == 0]
print(ex)

ex1 = [valor if valor % 2 == 0 and valor % 4 ==0 else 0 for valor in lista]
print(ex1)


nome="Victor Alexandre"
iterador=iter(nome)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

print('dentro do laço for')

for v in iterador:
    print(v)

ex5=(letra for letra in iterador)
for x in ex5:
    print(x)


from itertools import zip_longest,count

lista1=['a','b','c','d']
lista2=['e','f','g']
contador=count()
lista3 = zip(contador,lista1,lista2)
for x,y,z in lista3:
    print(x,y,z)



lista10=[1,2,3,4,5,6,7,8,9]
filtrado = [x for x in lista10 if x > 5]
print(filtrado)