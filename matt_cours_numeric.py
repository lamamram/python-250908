# %%
######## la seule conversion implicite entre types de données !=
entier = 33
PI = 3.14
# "+" travaille avec int et float
print(entier + PI)

# %%
######## CONVERSIONS EXPLICITES
age = input("saisir un âge")
# besoin de conversion EXPLICITE en int
age = int(age) + 1
# "+" avec str => concaténation
# surcharge d'opération le signe + peut être défini 
# pour plusieurs usages liés à des types !=
print("j'ai " + str(age) + " ans !")

# %%

