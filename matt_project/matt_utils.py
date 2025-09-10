"""
module de parsing variés

parse_template

...
"""

# ModuleNotFoundError
# from helpers.tools import debug

## tous les chemins d'import du projet doivent être calculés
## à partir du programme principal
# from matt_project.helpers.tools import debug

## OU demander explicitement un chemin relatif
# "." : package courant
# "..": package parent
from .helpers.tools import debug


DEFAULT = "N/A"

def parse_template(
    tpl: str, 
    data: dict, 
    delims: tuple=("{{", "}}"), 
    default: str=DEFAULT,
    **opts
  ) -> str:
  """
  interprète un template avec des données
  
  options **:
  debug=True
  ...
  """
  while tpl.find(delims[0]) != -1:
    start_index = tpl.index(delims[0]) + len(delims[0])
    end_index = tpl.index(delims[1])
    key = tpl[start_index:end_index]
    if "debug" in opts and opts["debug"]:
      print(debug("key", key))
    tpl = tpl.replace(delims[0] + key + delims[1], data.get(key, default))
  return tpl

# import et from ... import exécutent tout le code
# print("coucou")