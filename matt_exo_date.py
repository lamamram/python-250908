# %%
# 1. saisir un entier au clavier => compris entre 0 et 86400 (nb de secondes dans une journée)
# 2. convertir la sortie précédente en entier
# 3. décomposer ce nombre en nb en heure, minutes, secondes
# 4. affichier le résulat <nb_hour>h <nb_min>m <nb_sec>s

# %%
# nom de variable composé => snake_case != camelCase != PascalCase != kebab-case
nb_horaire = input("saisir un entier au clavier => compris entre 0 et 86400")
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

nb_horaire = input("saisir un entier au clavier => compris entre 0 et 86400")
nb_horaire = int(nb_horaire)

if 0 <= nb_horaire < 86400:
  nb_heure = nb_horaire // 3600
  nb_minute = (nb_horaire % 3600) // 60
  nb_seconds =nb_horaire % 60
  print(str(nb_heure) + "h " + str(nb_minute) + "m " + str(nb_seconds) + "s")
else:
  print( str(nb_horaire) + ": mauvaise valeur !")