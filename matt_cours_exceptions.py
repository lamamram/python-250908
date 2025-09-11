# %%

import random


# %%
###### problématique de la gestion d'erreur
# try: teste l'exécution du bloc ci dessous
# et s'interrompt et exécute le bloc except dès qu'une erreur == exception arrive
inconnue = random.randint(0,10)
try:
  numbers = list(range(5))
  print(numbers[inconnue])
except:
  print(f"{inconnue} out of the range")

# %%
###### capturer toutes les erreurs avec la classe Exception
## classe parente de toutes les erreurs
inconnue = random.randint(0,10)
try:
  numbers = list(range(5))
  print(numbers[inconnue])
except Exception as e:
  print(e, inconnue)
# %%
###### capturer plusieurs types d'erreurs !=
inconnue = random.randint(0,10)
denominateur = random.randint(0,2)
try:
  numbers = list(range(5))
  print(numbers[inconnue])
  print(1/denominateur)
except IndexError as ie:
  inconnue = len(numbers) -1
  print(f"rectification de IndexError: {numbers[inconnue]}")
except ZeroDivisionError as ze:
  denominateur += 1
  print(f"rectification de ZeroDiv: {1/denominateur}")
except Exception as e:
  print(e)

# %%
######## gestion commune pour plusieurs erreurs
inconnue = random.randint(0,10)
denominateur = random.randint(0,2)
try:
  numbers = list(range(5))
  print(numbers[inconnue])
  print(1/denominateur)
except (IndexError, ZeroDivisionError) as ce:
  inconnue = denominateur = 1
  print(f"rectification commune: {numbers[inconnue]} {1/denominateur}")
except Exception as e:
  print(e)

# %%
####### les mots clés else et finally
import random

inconnue = random.randint(0,10)
denominateur = random.randint(0,2)
try:
  numbers = list(range(5))
  print(numbers[inconnue])
  1/denominateur
except IndexError as e:
  print(e, inconnue)
# bloc exécuté s'il n'ya pas d'erreur (capturée ou non)
else:
  print("good ending !!")
finally:
  print("même si en cas de plantage !!")

print("continuer le programme")

# %%
###### raise: gestion personnalisé d'erreur  dans les fonctions
import random

def ratio_h_w(height, weight):
  if not weight:
    raise ValueError("poids nul")
  return height/weight

if __name__ == "__main__":
  try:
    ratio_h_w(random.randint(140, 220), 0)
  except ValueError as e:
    print(e)
    


# %%
