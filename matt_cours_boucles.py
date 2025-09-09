# %%
fruits = ["pomme", "Papaye", "cerise"]

fruits_p = []
for fruit in fruits:
  if fruit.lower().startswith("p"):
    fruits_p.append(fruit)

print(fruits_p)

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
