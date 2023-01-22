from utils.path_list import path_list

def location_menu():
  print("Onde deseja salvar o projeto?")
  path = path_list()
  suggestion = path[1] + "/" + path[2] + "/" + path[3] + "/"
  print("")
  print("1- " + suggestion)
  print("2- Outro lugar")
  print("")