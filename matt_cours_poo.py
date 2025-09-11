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
  # acc <=> self
  acc = Account()
  acc._id = 14343
  acc.balance = 100.
  acc.overdraft = 100.

  acc.withdrawal(50)
  print(acc.balance)

  ## attribut d'objet vs attribut de classe
  print(Account.balance)
  acc2 = Account()
  acc2.balance = 200.
  print(acc2.balance)

# %%
######## notion hasardeuse d'attributs / méthodes publics et privés
class Account:
  # attributs privés (inaccessible en lecture et écriture depuis l'extéreur de la classe)
  # privé => préfixé par "__"
  __id = 0
  __balance = 0.
  __overdraft = 0.

  # méthode publique
  def withdrawal(self, amount: float) -> dict:
    if amount > 0:
      self.balance -= amount
    else:
      print(f"montant invalide: {amount}")
  
  # getter et setter
  def get_id(self):
    return self.__id
  
  def set_id(self, _id):
    self.__id = _id


acc = Account()
# inaccessible en lecture depuis l'extérieur de la classe
# AttributeError
# print(acc.__id)
acc.__id = 13453
print(acc.get_id())
# le véritable attribut privé est accessible en public avec _Account__id
# == mauvaise POO
print(acc._Account__id)

# %%
####### class Account "acceptable"

class Account:
  """
  documentation de la classe
  """

  ## initalise les attributs d'objet au moment de l'instanciation
  def __init__(self, _id: int, balance: float=100, overdraft: float=100):
    self.__id = _id
    self.__balance = balance
    self.__overdraft = overdraft

  # pour le print et la conversion en str
  def __str__(self):
    return f"{self.__id}: balance: {self.__balance}"

  # addition de comptes
  def __add__(self, account: Account):
    return self.__balance + account.get_balance()

  def get_balance(self):
    return self.__balance

  # méthode publique: interface entre l'extérieur et les méthodes privées
  def withdrawal(self, amount: float) -> dict:
    if amount > 0:
      self.__set_balance(-amount)
    else:
      print(f"montant invalide: {amount}")

  # méthode privée: mettent à jour les attributs privés
  def __set_balance(self, amount: float):
    self.__balance += amount


if __name__ == "__main__":
  # effet du __init__
  acc = Account(_id=1433, balance=200.)
  acc.withdrawal(50)
  # effet du __str__
  print(acc)
  print(acc.__doc__)
  acc2 = Account(_id=34534, balance=300.)
  print(acc + acc2)

# %%
############ HERITAGE de classe (relation être)
from datetime import datetime
class Client:
  def __init__(self, f_name: str, l_name: str, date_joint: datetime):
    self.f_name = f_name
    self.l_name = l_name
    self.date_joint = date_joint

  def get_full_name(self):
    return f"{self.f_name.capitalize()} {self.l_name.upper()}"
  
  def format_date_joint(self, format):
    return self.date_joint.strftime(format)

cl = Client("joe", "smith", datetime.now())
print(cl.get_full_name(), cl.format_date_joint("%Y"))
# %%
