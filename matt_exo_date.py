# %%
# 1. saisir un entier au clavier => compris entre 0 et 86400 (nb de secondes dans une journée)
# 2. convertir la sortie précédente en entier
# 3. décomposer ce nombre en nb en heure, minutes, secondes
# 4. affichier le résulat <nb_hour>h <nb_min>m <nb_sec>s

# %%
# nom de variable composé => snake_case != camelCase != PascalCase != kebab-case
nb_horaire = input("saisir un entier au clavier => compris entre 0 et 86400")

# %%
# REM: python est un langage avec typage dynamique
# => le type d'une variable peut changer 
nb_horaire = int(nb_horaire)

## traitement conditionnel

# if <expression>:
if 0 <= nb_horaire < 86400:
  # dans le bloc if => le if est vrai
  nb_heure = nb_horaire // 3600
  nb_minute = (nb_horaire % 3600) // 60
  nb_seconds =nb_horaire % 60

  print(str(nb_heure) + "h " + str(nb_minute) + "m " + str(nb_seconds) + "s")
# elif <expr>: (else if)
else:
  print( str(nb_horaire) + ": mauvaise valeur !")
# sortie du bloc if => continuation du programme
print("FIN")
# %%
# expression logique
nb_horaire >= 0 and nb_horaire < 86400
# sucre syntaxique
0 <= nb_horaire < 86400
# A and B <=> not (not A OR not B) 
not (nb_horaire < 0 or nb_horaire >= 86400)

# %%

## contrôle de type : vérifier si la str est numérique => convertible en entier
if nb_horaire.isnumeric():
  nb_horaire = int(nb_horaire)

  if 0 <= nb_horaire < 86400:
    nb_heure = nb_horaire // 3600
    nb_minute = (nb_horaire % 3600) // 60
    nb_seconds =nb_horaire % 60
    print(str(nb_heure) + "h " + str(nb_minute) + "m " + str(nb_seconds) + "s")
  else:
    print( str(nb_horaire) + ": mauvaise valeur !")
else:
  print(nb_horaire + ": pas un entier !!!")
# %%

if nb_horaire.isnumeric() and 0 <= int(nb_horaire) < 86400:
  nb_horaire = int(nb_horaire)
  nb_heure = nb_horaire // 3600
  nb_minute = (nb_horaire % 3600) // 60
  nb_seconds =nb_horaire % 60
  # print(str(nb_heure) + "h " + str(nb_minute) + "m " + str(nb_seconds) + "s")
  ## TECHNIQUES DE FORMATAGE EN PYTHON
  # 1. print: conversion implicite et concaténation
  # print(nb_heure, "h", nb_minute, "m", nb_seconds, "s")
  # 2. templating à la sauce python2
  # print( "%dh %dm %ds" % (nb_heure, nb_minute, nb_seconds) )
  # 3. templating à la sauce python3
  print( "{}h {}m {}s".format(nb_heure, nb_minute, nb_seconds) )
  # 4. f-string: injecter directement des expression dans les str
  print( f"{nb_heure}h {nb_minute + 1}m {nb_seconds:02d}s" )
elif not nb_horaire.isnumeric():
  print(nb_horaire + ": pas un entier !!!")
else:
  print( str(nb_horaire) + ": mauvaise valeur !")
# %%
