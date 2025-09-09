# %%
## définition d'un dict
## collection de données (joe, 33, admin)
## accessible par des clés ("firstname, age, role")
user = {
  "firstname": "joe",
  "age": 33,
  "role": "admin"
}

# %%
# les clés peuvent être de n'importe quel type IMMUTABLE
points = {
  (-2.40032, 43.45453): "PARIS",
  (1.3434, 40.4545): "MARSEILLE"
}

# %%
# lecture des données
user["firstname"], user["age"]
points[(-2.40032, 43.45453)]
# %%
# écrire: modifier et créer des paires clés/valeurs
user["lastname"] = "SMITH"

# %%
# KeyError: clé absente
# user["date_joint"]

# in fonctionne pour les dict avec les clés
if "date_joint" in user:
  print(user["date_joint"])
else:
  print("N/A")
# %%
# la valeur de la clé si celle ci existe ou une valeur par défaut
user.get("date_joint", "N/A")
# %%
# boucler sur un dictionnaire
# a priori avec les clés
for key in user:
  print(key)

# sur les valeurs
for val in user.values():
  print(val)

# sur les paires clé / valeur
for key, val in user.items():
  print(key, val)
# %%
# list de tuple <=> dict
list_tup = list(user.items())
list_tup

dict(list_tup)
# %%
# zip: créer un dict à partir de 2 listes de clés et de valeurs
keys = list(user)
values = list(user.values())
keys, values

dict(zip(keys, values))
# %%
