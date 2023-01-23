import os

def commands(new_path, action):
  commands_list = {
    "directory_exist": os.path.exists(new_path),
    "mkdir": "mkdir " + new_path,
    "mkdir_back": "mkdir " + new_path + "/back",
    "react": "npx create-react-app " + new_path + "/web",
    "npm_init": "cd ~ && cd " + new_path + "/back && npm init -y",
  }

  return commands_list[action]