import os

def path():
  path = os.getcwd()
  path_list = path.split("/")
  return "/" + path_list[1] + "/" + path_list[2] + "/" + path_list[3] + "/"