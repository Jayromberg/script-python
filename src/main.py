# import os
from menu.home_menu import home_menu
from menu.location_menu import location_menu
from utils.path_list import path_list

def project_location():
  location_menu()

  option = input("Digite sua opção: ")

  if option == "1":
    print(path_list())
  elif option == "2":
    print('oi')
  else:
    print("Não conheço este comando")
    exit(-1)
  

print("Bem-vindo(a) ao instalador automático de dependências. Por favor, escolha a opção desejada:")
home_menu()
project_category = input()

if project_category == "0":
  print("Saindo do programa...")
  exit(0)
elif project_category == "1":
  project_location()
else:
  print("Não conheço este comando")
  exit(-1)

# os.system("pwd")

# os.system("clear")

