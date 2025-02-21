import os

os.system("clear")

#Solicitando dados 

numero_um = int(input("digite um numero: "))
operacao = input("digite a operaçao desejada: ")
numero_dois = int(input("digite um numero: "))

# Verificando

match operacao:
    case "+":
        resultado = numero_um + numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "/":
        resultado = numero_um / numero_dois
    case _:
        print("opcao invalida.")

# Resultados

print()        
print(f"primeiro numero: {numero_um}")
print(f"Operaçao: {operacao}")
print(f"segundo numero: {numero_dois}")
print(f"Resultado: {resultado}")