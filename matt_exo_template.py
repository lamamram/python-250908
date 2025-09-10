"""
exercice : remplacer les clés entourées par "((" et "))"
dans un texte par les valeurs correspondantes dans un dico

1. afficher le contenu entre la première occurence de (( et ))
2. remplacer ((pression)) par 500 dans _template
Hint: regarder la fonction str.replace
3. itérer sur _template pour remplacer toutes les slots (())
par la clé correspondante si celle ci existe ou par N/A
"""

# %%

_template = """
robinet.pression=((pression))
robinet.section=((section))
robinet.debit=((debit))
robinet.capacite=((capacite))
"""

injections = {
    "pression": "500",
    "section": "30",
    "debit": "2"
}

# %%

# 3/ faire boucler ce bout de code tant qu'on ait au - une paire de motifs '(('
while _template.find("((") != -1:
  # 1/ trouver les premières occurence des motifs '((' et '))' dans _template
  start_index = _template.index("((") + len("((")
  end_index = _template.index("))")
  key = _template[start_index:end_index]
  # 2/ remplacer ((pression)) par 500 dans _template
  _template = _template.replace("((" + key + "))", injections.get(key, "N/A"))

print(_template)
# %%
##### encapsuler le code ci-dessus pour en faire une fonction réutilisable

# 1/ donner un nom signifiant
# 2/ choisir les paramètres centraux/essentiels et les paramètres qui peuvent avoir une valeur par défaut
# 3/ effectuer le refactoring (chercher + remplacer les variables ou valeurs en dur du code en paramètres)
# 4/ gérer la sortie de la fonction
## tester avec un cas d'exemple
# 5/ utiliser le ** pour mettre un mode "debug"

_tpl = """
blablabla .... {{key1}}
blablabla .... {{key2}}
"""

data = {
  "key1": "val1",
  "key2": "val2",
  "key3": "val3",
}


def parse_template(
    tpl: str, 
    data: dict, 
    delims: tuple=("{{", "}}"), 
    default: str="N/A",
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
      print(f"DEBUG: key: {key}")
    tpl = tpl.replace(delims[0] + key + delims[1], data.get(key, default))
  return tpl

parse_template(_template, injections, delims=("((", "))"))
parse_template(_tpl, data)
# %%
