import os

def menu():
	print("1- Front-End")
	print("2- Back-End")
	print("3- Mobile")
	print("0- Sair")
	print("")

print("Bem-vindo(a) ao instalador automático de dependências. Por favor, escolha a opção desejada:")
menu()
project_category = input()

if project_category == "0":
  print("Saindo do programa...")
  exit(0)
else:
  print("Não conheço este comando")
  exit(-1)

# os.system("pwd")

# os.system("clear")

