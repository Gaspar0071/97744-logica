import os

os.system("clear")

# Solicitando dados 
quantidade_maca = int(input("digite a quantidade de maças desejadas: "))

# Verificando
if quantidade_maca < 12:
    preco_maca = 1.30
else:
    preco_maca = 1.00    

valor_total = quantidade_maca * preco_maca

# Resultado

print()
print(f"valor total da compra R$ {valor_total:.2f}")