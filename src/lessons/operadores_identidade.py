# Operador de identidade(is ou is not) verifica se dois objetos ocupa a mesma região de memória
saldo = 500
limite = 500

# O saldo ocupa a mesma região de memória do limite?
print(saldo is limite)

# O saldo não ocupa a mesma região de memória do limite?
print(saldo is not limite)
