# %%
# affectation de la valeur 1 entier dans la variable x
# on met 1 dans x
# x <= 1
# "=" : opérateur d'affectation
x = 1
# %%
# on ne peut pas déclarer les variables en python
# NameError
# y
# %%
# distinction entre instruction et expression
# EXPRESSION : n'importe quelle écriture en python EVALUABLE
# truc qu'on peut mettre dans un print sans planter
# valeurs litérales => expr
print(1)
# variable => expr
print(x)
# n'importe quelle association de var & valeur & operateur & fonction ...
print(x + 1)

# INSTRUCTION: ligne de code
# ex: l'affectation n'est pas une expression
# TypeError
# print(y = 2)
# %%
# mécanismes d'affectation communs
x = 1
y = 1
# OU
y = x
# id(x) : appel d'une fonction est une expression
# id(x) == id(y): comparaison est une expression booléenne
# x is y idem que au dessus
print(id(x), id(y), id(x) == id(y), x is y)
# incrémentation => + 1
y = y + 1
# idem que au dessus
y += 1
# maintenant x et y ne ciblent plus la même case mémoire
print(id(x), id(y), x is y)
# %%
# types principaux
# int
entier = 33
# float: nombre réel
PI = 3.14
# str
firstname = "joe"
# bool
faux = False
# list: collection de valeurs de type != et indexable
tensions = [117, 78]
bilan = [1.76, 64, "A+", tensions]
# tuple: collection // MAIS NON MODIFIABLE => t-uplet (x, y, z, t) => quadr-uplet 
point = (-2.40032, 43.45453, "PARIS")
# 
user = {"firstname": firstname, "age": entier, "bilan": bilan}

# %%
# manipulations usuelles avec les variables
print(tensions)
print(point)
print(user)

# paramètres sep & end de print
# types de saut de lignes (linux, windows, Mac OS)
# CR : Carriage Retrurn => \r
# LF: Line Feed => \n
# en Linux => saut de ligne => LF \n
# en windows => // > CRLF => \r\n compatible LF
# en MAcos => // CR > \r
# %%
# saisie au clavier
saisie = input("nombre: ")
# afficher le type d'une variable
# ATTENTION !! input retourne une str
print(saisie, type(saisie))
# %%
# introspection
# help: documentation gérée par VSCODE via l'extension python
# help(print)
# dir => affiche les variables et/ou fonctions INTERNES aux variables
print(dir(saisie))
# ex.
print(saisie.upper())

# alléger variable sans supprimer
# None => réprésentation de rien
saisie = None
# libérer == supprimer les variable
del saisie
# print(saisie)
# %%
