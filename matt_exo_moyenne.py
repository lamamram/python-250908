"""
1/ saisir n valeurs entiers relatifs séparés par ","
2/ on veut itérer sur les valeurs pour vérifier
que ces valeurs sont des entiers relatifs
3/ si c'est convertible on ajoute la valeur convertie dans une liste
3b/ si ce n'est pas convertible => "casser la boucle"
4/ calculer la moyenne depuis la liste
5/ présenter le résultat avec 2 chiffres sign.  
"""

# %%
valeurs = input("n valeurs entiers relatifs séparés par ','")
valeurs = valeurs.split(",")


numbers = []
for valeur in valeurs:
  # trim: nettoyer les espaces possibles à gauche et à droite d'une valeur
  valeur = valeur.strip()
  # convertible en entier relatif: positif OU négatif
  # négatif == commence avec - ET le reste est numérique
  if valeur.isnumeric() or ( valeur.startswith("-") and valeur[1:].isnumeric()):
  # if valeur.isnumeric() or ( valeur[0] == "-" and valeur[1:].isnumeric()):
    numbers.append(int(valeur))

# vérifier que la liste est non vide
# if len(numbers) != 0:
if numbers:
#   print(f"moyenne de {numbers}: {sum(numbers) / len(numbers):.2f}")
  print(f"moyenne de {numbers}: {round(sum(numbers) / len(numbers), 2)}")
else:
  print("pas de nombres à calculer")
# %%

valeurs = input("n valeurs entiers relatifs séparés par ','")
valeurs = valeurs.split(",")


numbers = []
for valeur in valeurs:
  valeur = valeur.strip()
  if valeur.isnumeric() or ( valeur.startswith("-") and valeur[1:].isnumeric()):
    numbers.append(int(valeur))
  else:
    print(f"{valeur}: pas un entier !!")
    break
# si l'iterable "valeurs" a été complètement consommé
# autrement dit pas de break rencontré
else:
  if numbers:
    print(f"moyenne de {numbers}: {round(sum(numbers) / len(numbers), 2)}")
  else:
    print("pas de nombres à calculer")


# %%
