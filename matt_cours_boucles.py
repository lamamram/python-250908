# %%
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
