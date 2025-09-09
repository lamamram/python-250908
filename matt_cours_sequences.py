# %%
## SEQUENCE => str, list, tuple

dicton = "appeler un chat un chat"
mots = ["appeler", "un", "chat", "un", "chat"]
tups = tuple(mots)

print(dicton, mots, tups)
# %%
## opérateur []: lire les éléments d'une séquence à l'index i
# 0-indexed => 1er index de la séquence
## REM: cette expression est un tuple implicite
dicton[0], mots[0], tups[0]

# un type de données utilsant [] avec des entiers est dit INDEXABLE
# %%
# dernier élément: nb d'éléments - 1
len(dicton), len(mots)
dicton[len(dicton) - 1]

# les séquences peuvent être ordonnées à partir du dernier éléments
# à partir -1
dicton[-1], dicton[-len(dicton)] , mots[-1]
# %%
# diff entre les listes et les tuples
# diff entre mutabilité et immutabilité

# mutabilité: modification partielle et interne de la liste
mots[0] = "dénoncer"
print(mots)

# immutabilité: pas de modification en interne
# TypeError
# tups[0] = "villipender"
# corollaire: pour changer la variable, on la réaffecte complètement 
tups = ("villipender", "un", "chat", "un", "chat")

# %%
# les str sont immutables
# dicton[0] = "vitupérer"
dicton = "vitupérer un chat un chat"
# %%
# trouver une sous-séquence: faire un SLICING
# 10 => 'u', 17 => ' '
# l'indice de début est compris, l'indice de fin n'est pas compris 
dicton[10:17], mots[1:3]
# %%
# retourner l'indice de premier occurence d'une séquence
dicton.index("un"), dicton.find("chat")

start_index = dicton.index("un")
end_index = dicton.find("chat") + len("chat")
dicton[start_index:end_index]

# %%
# slicing remarquables
# à partir du début jusqu'à chat
mots[:mots.index("chat")]
# à partir de chat jusqu'à la fin
mots[mots.index("chat"):]
# slicing tous les 2 éléments
mots[::2]
# inverser la séquence
mots[::-1]
# %%
# savoir si un élément existe dans une séquence: opérateur in
"chat" in dicton, "chien" not in mots
# %%
## boucle for: itérer sur les éléments d'une séquence

mots = ["appeler", "un", "chat", "un", "chat"]

# je veux mettre chaque mot de la liste en majuscule
# POUR chaque élément DANS la liste je transforme l'élément en majuscule
for mot in mots:
  print(mot.upper())

print(mots)

# un type de données qui peut être mis dans une boucle est dit ITERABLE
# %%
# ajouter des éléments dans une liste
# liste vide, str vide => "", tuple vide ()
mots = []
# IndexError: on ne peut pas créer les indice
# mots[0] = "appeler"
# ajouter à la fin: 
# action mutable: action en interne mais ne retourne rien
print(mots.append("un"))
# ajouter à gauche
mots.insert(0,"appeler")
# concaténer les listes
# mots = mots + ["chat", "un", "chat"]
# mots += ["chat", "un", "chat"]
mots.extend(["chat", "un", "chat"])
mots
# %%
# ajouter des éléments dans une liste
# enlever à la fin ET retourne
print(mots.pop())
# à gauche
mots.pop(0)
mots

# %%

mots.remove("un")
mots

# %%
# transformation de str en liste et réciproquement

dicton = "appeler un chat un chat"
mots = dicton.split()

# pour chaque mot je veux ajouter les mot de longueur >= 3 dans une liste finale
results = []
for mot in mots:
  if len(mot) >= 3:
    results.append(mot)

print(results)

# remettre la liste de mot en tant que str
# results.join(" "): contre intuitif
" ".join(results)
# %%
## UNPACKING d'un tuple

tup = ("joe", "SMITH", 33)
firstname, lastname, age = tup
firstname, lastname, age

# %%
# firstname = "joe"
# lastname = "SMITH"
# age = 33
firstname, lastname, age = "joe", "SMITH", 33
firstname, lastname, age

# %%
