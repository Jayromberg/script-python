# import os
from menu.home_menu import home_menu
from menu.project_path import project_path

print("Bem-vindo(a) ao instalador automático de dependências. Por favor, escolha a opção desejada:")
home_menu()
project_category = input()

if project_category == "0":
  print("Saindo do programa...")
  exit(0)
elif project_category == "1":
  chosen_path = project_path()
else:
  print("Não conheço este comando")
  exit(-1)

# os.system("pwd")

# os.system("clear")

