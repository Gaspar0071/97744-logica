import os

os.system("clear")

# SOLICITANDO DADOS
login = str(input("digite seu email: "))
senha_2 = int(input("digite sua senha: "))

login = "gaspar77"
senha = 2508

if login == login and senha == senha_2:
  print("Bem-vindo, ja olhou a cortina do seu quarto pra ver se esta tudo certo?")    
else:
  print("login invalido")  