# %%
# appliquer une fonction à un vecteur

numbers = list(range(1, 11))
numbers

def square(x: float):
  return x ** 2

def mon_map(func, it):
  for i in range(len(it)):
    it[i] = func(it[i])
  return it

# programmation fonctionnelle: composée de fonction
mon_map(square, numbers)

# %%
######## fonction lambda vs fonction nommée
# lambda: fonction sans nom, qui retourne une unique EXPRESSION
numbers = list(range(1, 11))
mon_map(lambda x: x**2, numbers)

# %%
######## map(): appliquer une fonction à un itérable
numbers = list(range(1, 11)) 
list(map(lambda x: x**2, numbers))

# %%
######## filter(): filtrer un itérable selon la valeur de retour VRAIE d'une fonction
numbers = list(range(1, 11))
list(filter(lambda x: x % 2, numbers))

# %%
######## sorted(): trier un itérable selon le retour d'une fonction
import random

rows = [ f"row_{i}" for i in range(20) ]
random.shuffle(rows)
# trier selon l'entier contenu dans la str
sorted(rows, key=lambda r: int(r[4:]))
# %%
