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
  for line in reader:
    print(line)




# %%
