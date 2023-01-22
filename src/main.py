# import os
from menu.home_menu import home_menu
from menu.project_path import project_path
from menu.project_name import project_name
from commands.font_end import front_end_commands

print("Bem-vindo(a) ao instalador automático de dependências. Por favor, escolha a opção desejada:")
home_menu()
project_category = input()

if project_category == "0":
  print("Saindo do programa...")
  exit(0)
elif project_category == "1":
  chosen_path = project_path()
  chosen_name = project_name()
  front_end_commands(chosen_path, chosen_name)
else:
  print("Não conheço este comando")
  exit(-1)

# os.system("pwd")

# os.system("clear")

