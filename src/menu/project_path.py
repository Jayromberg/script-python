from menu.location_menu import location_menu
from utils.path import path

def project_path():
  location_menu()
  option = input("Digite sua opção: ")
  if option == "1":
    return path()
  elif option == "2":
    manual_path = input("Digite o path ou araste para o terminal a pasta que deseja salvar o projeto: ")
    return manual_path
  else:
    print("Não conheço este comando")
    exit(-1)