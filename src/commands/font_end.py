import os

def front_end_commands(path, project_name):
  command_mkdir = "mkdir " + path +  project_name
  os.system(command_mkdir)
  command_react = "npx create-react-app " + path + project_name + "/web"
  os.system(command_react)