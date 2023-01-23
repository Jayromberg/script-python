from menu.home_menu import home_menu
from commands.font_end import front_end_commands
from commands.back_end import back_end_commands

print("Bem-vindo(a) ao instalador automático de dependências. Por favor, escolha a opção desejada:")
home_menu()
project_category = input()

if project_category == "0":
  print("Saindo do programa...")
  exit(0)
elif project_category == "1":
  front_end_commands()
elif project_category == "2":
  back_end_commands()
else:
  print("Não conheço este comando")
  exit(-1)
