# Controla o fluxo do código (if, elif e else)

opcao = input("Digite a opção (1 ao 3): ")

if opcao == 1:
    print("Opção 1")
elif opcao == 2:
    print("Opção 2")
else:
    print("Opção 3")

# Program to demonstrate ternary operator
a = 10
b = 20

# python ternary operator
min = "a is minimum" if a < b else "b is minimum"

print(min)
