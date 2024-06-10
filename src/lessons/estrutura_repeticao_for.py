# For
palavra = 'Videogame'
vogais = 'AEIOU'
consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'

for letra in palavra:
    print(f'Letra: {letra}')

# For else
print(f'Vogáis:', end=" ")
for letra in palavra:
    if letra.upper() in vogais:
        print(letra, end=", ")
else:
    print()
    print("fim")

# For range(range object)

lista = list(range(10))
print(lista)

# Multiplo de um número
inicio = 0
fim = 71
incrimento = 7

for multiplo in range(inicio, fim, incrimento):
    print(multiplo, end=", ")
