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

# docstring: """ """
def ma_fonction(param: str) -> str:
  """
  incroyable fonction qui transforme en majuscule
  """
  return param.upper()

maj = ma_fonction("bonjour")
maj
# les annotations n'empêchent pas l'erreur
# ma_fonction(3.14)
# %%
# portée d'une variable globale à une fonction
def ma_fonction(param: str) -> str:
  return f"{param.upper()}  {person}"

# variable globale à la fonction
person = "matt"

# la variable person a été créée 
# avant d'être utilsée dans le bloc de la fonction
ma_fonction("bonjour")

# %%
# portée d'une variable locale à une fonction
def ma_fonction(param: str) -> str:
  # CE person est local dans la fonction
  person = "joe"
  print(id(person))
  return f"{param.upper()}  {person}"

# CE person est global
person = "matt"

print(ma_fonction("bonjour"), person, id(person))
# %%
# forcer la maj d'une variable globale dans une fonction
def ma_fonction(param: str) -> str:
  global person
  person = "joe"
  print(id(person))
  return f"{param.upper()}  {person}"

person = "matt"

print(ma_fonction("bonjour"), person, id(person))
# %%
# paramètres positionnels / obligatoire et optionnels / nommés
def ma_fonction(pos, opt="default"):
  return pos, opt

print(ma_fonction("pos", "opt"))
# TypeError: pos n'a pas de valeur initialisée
# ma_fonction()
ma_fonction("pos")
# %%
# ordre des paramètres positionnels à gauche et nommé après

# SyntaxError
# def ma_fonction(opt="default", pos):
#   return opt, pos

# %%
# on peut également nommés les paramètres à l'appel
def ma_fonction(pos, pos2):
  return pos, pos2

# flécher les valeurs aux paramètres 
# indépendemment de l'ordre des paramètres de la définition
ma_fonction(pos2="pos2", pos="pos")
# %%
