import json
import shutil
import tempfile

def script_dev(path):
  with open(path +'/back/package.json', 'r', encoding='utf-8') as arq, \
    tempfile.NamedTemporaryFile('w', delete=False) as out:
    # ler todo o arquivo e obter o objeto JSON
    dados = json.load(arq)
    # atualizar os dados com a nova pergunta
    dados["scripts"] = {
      "dev": "npm alguma coisa",
    }
    # escreve o objeto atualizado no arquivo temporário
    json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))
  # se tudo deu certo, renomeia o arquivo temporário
  shutil.move(out.name, path +'/back/package.json')
