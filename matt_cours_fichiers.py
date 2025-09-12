# %%
###### créer un fichier en python: open()
## REM: depuis python3 python est en utf-8 par défaut
f = open("./matt_mon_fic.txt", mode="w", encoding="utf-8")
print(f.write("1ère line\n"))
## tout ce qui est ouvert doit être fermé => fuites de mémoire
f.close()

# %%
####### lire le fichier
f = open("./matt_mon_fic.txt", mode="r", encoding="utf-8")
print(f.read(6))
# gestion d'un curseur
print(f.read())
f.close()

# %%
######## écriture à la fin + gestionnaire de contexte WITH
with open("./matt_mon_fic.txt", mode="a", encoding="utf-8") as f:
  f.write("2nd line\n")

## fichier fermé
# ValueError
# f.write("ko")



# %%
##### itération sur un fichier
with open("./matt_mon_fic.txt", mode="r", encoding="utf-8") as f:
  # print(f.readlines())
  # for line in f:
  #   print(line)
  print(list(f))

# %%
# lecture et écriture
# un curseur au début pour la lecture
# et un curseur à la fin pour l'écriture
with open("./matt_mon_fic.txt", mode="r+", encoding="utf-8") as f:
  f.read(10)
  f.write("3rd line\n")

# %%
########### attention avec le méthodes bas-niveau qui gère des octets et non des caractères
with open("./matt_mon_fic.txt", mode="r", encoding="utf-8") as f:
  # déplacement de 2 octets, or "è" est codé avec 2 octets et le 1 avec 1 octet
  # le curseur est mal positionné au milieu d'un caractère
  f.seek(2)
  # UnicodeDecodeError
  # f.read(10)

# %%
###########

content = "mon contenu à mettre en binaire"
# pas de gestion de l'encodage
b_content = b'mon contenu a mettre en binaire'
# str => bytes
b_content = bytes(content, encoding="utf-8")
with open("./matt_mon_bin", mode="wb") as f:
  f.write(b_content)

with open("./matt_mon_bin", mode="rb") as f:
  # bytes => str
  content = f.read().decode("utf-8")

# %%
####### réouvrir une variable gérée par un gestionnaire de contexte
with open("./matt_mon_fic.txt", mode="r", encoding="utf-8") as f:
  print(f.read())

### fermé
# ici on ne peut pas le faire
with f:
  # ValueError
  print(f.read())

# %%
