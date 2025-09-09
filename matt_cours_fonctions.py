# %%
# définition d'une fonction
def ma_fonction():
  print("coucou")

# appel de la fonction: exécution du bloc de la définition
# ma_fonction est un objet de type fonction
# (): opérateur d'appel
# les fonctions sont des objets callables
print(ma_fonction())
# la valeur de l'appel est None car le bloc ne retourne rien
# %%
# valeur de retour d'une fonction
def ma_fonction():
  return "coucou"
  # jamais exécuté car return arrête le bloc
  print("continue")

print(ma_fonction())

# %%
# param: paramètre à initialiser au moment de l'appel
def ma_fonction(param):
  return param.upper()

maj = ma_fonction("bonjour")
# AttributeError
# ma_fonction(3.14)
# %%
# ajouter des annotations aux fonctions
# pure information (pas un check)
# permet l'autocomplétion de VsCode
def ma_fonction(param: str) -> str:
  return param.upper()

maj = ma_fonction("bonjour")
maj
# les annotations n'empêchent pas l'erreur
# ma_fonction(3.14)
# %%
