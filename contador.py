from itertools import count

contador = count(start=1,step=1)
lista=['A','B','C','D','E']
lista = zip(contador,lista)
print(list(lista))

contador = count(start=1,step=1)
for valor in contador:
    if valor == 10:
        break
    print(valor)


from itertools import combinations,permutations,product

#A ordem não importa

letras = ['a','b','c','d','e','f']
grupo=2
for combinacao in combinations(letras,grupo):
    print(combinacao)

#A ordem importa
for combinacao in permutations(letras,grupo):
    print(combinacao)

#A ordem importa e repete as letras
for combinacao in product(letras,repeat=3):
    print(combinacao)




valores = [1,2,3,4,5,6,7,8,9]

multiplicado = list(map(lambda x : x*2,valores))
print(multiplicado)

produtos = [
    {'nome':'p1', 'preco':2},
    {'nome':'p2', 'preco':12},
    {'nome':'p3', 'preco':23},
    {'nome':'p4', 'preco':42},
    {'nome':'p5', 'preco':66},
    {'nome':'p6', 'preco':15},
    {'nome':'p7', 'preco':65},
    {'nome':'p8', 'preco':44},
    {'nome':'p9', 'preco':54},
]

def aumenta(p):
    p['preco']=round(p['preco'] * 1.05, 2)
    return p

novos_preco = map(aumenta ,produtos)

for p in novos_preco:
    print(p)






















