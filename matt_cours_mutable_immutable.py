# %%
###### modification d'une variable immutable (str, tuple, int, float, ...)

dicton = "qui dort mange"
print(dicton.replace("mange", "dîne"))
print(dicton)
# pour modifier dicton il faut la réaffecter
dicton = dicton.replace("mange", "dîne")
# %%
###### modification d'une variable mutable (list, dict)
mots = ["qui", "dort", "mange"]
mots[2] = "dîne"
# action mutable qui change mots mais ne retourne rien
print(mots.remove("dîne"))
mots

# %%
###### cas du pop: modifie ET retourne
mots = ["qui", "dort", "mange"]
while mots:
  print(mots.pop())
mots

# %%
####### PIEGE: des affectations de list et de dict

mots = ["qui", "dort", "mange"]
# je me donne une copie de la liste
mots2 = mots
# action mutable
mots2[2] = "dîne"

print(mots, mots is mots2)
# %%
####### COPIE CREUSE de list et dict: .copy()

mots = ["qui", "dort", "mange"]
# mot2 est une copie indépendante de mots en mémoire
mots2 = mots.copy()

mots2[2] = "dîne"

print(mots, mots is mots2)

# %%
