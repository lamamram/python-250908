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
