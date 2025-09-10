# %%
######## BOUCLE CLASSIQUE
fruits = ["pomme", "Papaye", "cerise"]

fruits_p = []
for fruit in fruits:
  if fruit.lower().startswith("p"):
    fruits_p.append(fruit)

print(fruits_p)
del fruits
# %%
# boucle normale en C
# for ( condition initiale; condition d'arrêt; ce qui change )
# for(int i=0;i<100;i++){
#   printf("%d", i);
# }

# créer un compteur 1 => 100
# counter = [1, 2, 3, , ...., 100]
for i in range(100):
  print(i)

print(list(range(10)))
# %%
# types de ranges
for i in range(1, 11):
  print(i)

for i in range(1, 11, 2):
  print(i)

for i in range(10, -1, -1):
  print(i)
# %%
# transformer une liste en place (inline)
fruits = ["pomme", "Papaye", "cerise"]

for i in range(len(fruits)):
  fruits[i] = fruits[i].upper()

print(fruits)

# %%
#idem avec la fonction enumerate()
fruits = ["pomme", "Papaye", "cerise"]
# objet enumerate: proche à une liste de tuple à 2 éléments
print(list(enumerate(fruits)))
for i, fruit in enumerate(fruits):
  fruits[i] = fruit.upper()

print(fruits)

# %%
# liste en intension: une liste décrite par un plan de construction 
# ==  liste en compréhension
# NON par des valeurs litérales
fruits = ["pomme", "Papaye", "cerise"]

# je veux la liste des fruits en majuscules 
# POUR "fruit" pris DANS la liste "fruits"
# SI fruit commence en p ou P
fruits = [ fruit.upper() for fruit in fruits if fruit.lower().startswith("p") ]
fruits
# %%

# BOUCLE WHILE
# boucler un bloc d'instructions tant qu'une condition reste VRAIE
# le bloc du while doit modifier la condition SINON on a une boucle INFINIE
temp = int(input("temp °C"))

while temp < 100:
  print(f"{temp}: çà fonctionne")
  temp = int(input("temp °C"))

print("BOOM")


# %%
# les mots continue, break, else et pass pour while et for
# break sort directement de la boucle 
# pass : instruction qui ne fait rien (bouche trou / factotum)

temp = int(input("temp °C"))

while temp < 100:
  # pass
  if temp == 42:
    print("valeur maudite !")
    break
  if temp <= 33:
    print(f"{temp}: trop froid")
    temp += 10
    # interrompt le bloc courant et commence l'itération suivante
    continue
  print(f"{temp}: çà fonctionne")
  temp = int(input("temp °C"))
# exécute le bloc ci-dessous SI la boucle s'arrête normalement
# Si la boucle ne rencontre pas de break
else:
  print("trop chaud ! BOOM")



# %%
