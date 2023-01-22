import os

def front_end_commands(path, project_name):
  directory_exist = os.path.exists(path + project_name)
  command_mkdir = "mkdir " + path +  project_name
  command_react = "npx create-react-app " + path + project_name + "/web"

  if directory_exist:
    os.system(command_react)
  else:
    os.system(command_mkdir)
    os.system(command_react)
    