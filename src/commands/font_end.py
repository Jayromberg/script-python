import os
from commands.commands_list import commands
from menu.project_path import project_path
from menu.project_name import project_name

def front_end_commands():
  chosen_path = project_path()
  chosen_name = project_name()

  new_path = chosen_path + chosen_name
  
  directory_exist = commands(new_path, "directory_exist")

  if not directory_exist:
    os.system(commands(new_path, "mkdir"))
  
  os.system(commands(new_path, "react"))
    