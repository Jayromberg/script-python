import os

def back_end_commands(path, project_name):
  directory_exist = os.path.exists(path + project_name)
  command_mkdir = "mkdir " + path +  project_name 
  command_mkdir_back = "mkdir " + path + project_name + "/back"
  command_npm_init = "cd ~ && cd " + path + project_name + "/back && npm init -y" 

  if directory_exist:
    os.system(command_mkdir_back)
    os.system(command_npm_init)
  else:
    os.system(command_mkdir)
    os.system(command_mkdir_back)
    os.system(command_npm_init)