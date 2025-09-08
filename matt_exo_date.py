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
nb_heure = nb_horaire // 3600
nb_minute = (nb_horaire % 3600) // 60
nb_seconds =nb_horaire % 60

print(str(nb_heure) + "h " + str(nb_minute) + "m " + str(nb_seconds) + "s")
# %%
