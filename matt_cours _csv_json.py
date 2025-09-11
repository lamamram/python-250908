# %%
######### écriture d'un csv
import csv

header = ["name", "age", "sex", "role"]
users = [["bob", 32, "M;F", "dev"], ["jane", 28, "F", "admin"]]

# désactiver le saut de ligne en fin de ligne avec le writer csv sur WINDOWS
with open(
  "./matt_users.csv", 
  mode="w", 
  encoding="utf-8",
  newline=""
) as f:
  writer = csv.writer(f, delimiter=";", quotechar='"')
  writer.writerow(header)
  writer.writerows(users)

# %%
############## csv en lecture
with open(
  "./matt_users.csv", 
  mode="r", 
  encoding="utf-8",
) as f:
  reader = csv.reader(f, delimiter=";")
  # reader est un itérable
  # itération pas à pas
  header = next(reader)
  print(header)
  # reste des itérations
  for line in reader:
    print(line)

# %%
# classe itérateur

class MyIterator:
  ## initialiser la condition d'arrêt
  def __init__(self, limit=10):
    self.limit = limit
  
  # au début du for (ou next) créer le compteur
  def __iter__(self, counter=0):
    self.counter = counter
    # retourner l'objet
    return self
  
  def __next__(self):
    if self.counter >= self.limit:
      # lever une exception
      raise StopIteration
    ret = self.counter
    # condition de changement entre itération
    self.counter += 1
    return ret

it = MyIterator()
for i in it:
  print(i)

# %%
########### json / dict
import json

header = ["name", "age", "sex", "role"]
users = [["bob", 32, "M;F", "dev"], ["jane", 28, "F", "admin"]]

## vers une liste de dictionnaires
users = list(map(lambda user: dict(zip(header, user)), users))
print(users)

# écriture
with open("./matt_users.json", mode="w", encoding="utf-8") as f:
  json.dump(users, f)

# lecture
with open("./matt_users.json", mode="r", encoding="utf-8") as f:
  users = json.load(f)

header = list(users[0].keys())
header
# %%
