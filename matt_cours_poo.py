# %%
####### implementation d'une gestion bancaire en impératif

def withdrawal(acc: dict, amount: float) -> dict:
  if amount > 0:
    acc["balance"] -= amount
  else:
    print(f"montant invalide: {amount}")
  return acc

if __name__ == "__main__":
  account = {
    "_id": 14434534,
    "balance": 100.,
    "overdraft": 100.
  }
  account = withdrawal(account, -50)
  print(account)

# %%
##### première écriture en POO
class Account:
  # attributs
  _id = 0
  balance = 0.
  overdraft = 0.

  # méthodes
  ## pour chaque méthode: le premier paramètre obligatoire est self
  ## qui représente l'objet instancié de la classe
  def withdrawal(self, amount: float) -> dict:
    if amount > 0:
      self.balance -= amount
    else:
      print(f"montant invalide: {amount}")

if __name__ == "__main__":
  # instanciation: création d'un objet de la classe Account
  acc = Account()
  acc._id = 14343
  acc.balance = 100.
  acc.overdraft = 100.

  acc.withdrawal(50)
  acc.balance

# %%
