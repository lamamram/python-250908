# %%
####### utiliser l'interface DbAPI en python
## client simples pour les sgdb usuels
# PyMySQL (pip)
# pip install "psycopg[binary]" (PostGre)

## ORM : Object Relational Mapper
# librairie qui piloter le SQL à partir de classe (no SQL)
# SQLAlchemy


import sqlite3

# connect
with sqlite3.connect("../dns.db") as conn:
  ## cur
  ## par défaut, le curseur fetch des tuples 
  ## on peut un "dict" en résulant
  conn.row_factory = sqlite3.Row
  cur = conn.cursor()
  # execute
  cur.execute("SELECT SQLITE_VERSION() AS version")
  # fetch
  row = cur.fetchone()
  print(dict(row))

# close
# %%
######## insertion des tables à partir d'un script
import os, sqlite3

def execute_script(script_path, conn: sqlite3.Connection):
  if not os.path.exists(script_path):
    raise FileNotFoundError("script absent")
  with open(script_path, "r", encoding="utf-8") as sql_f:
    script = sql_f.read()
  ## contexte réentrant (multiple with) pour être sûr d'être ouvert
  with conn:
    cur = conn.cursor()
    try:
      cur.executescript(script)
      return True, "OK"
    except sqlite3.OperationalError as oe:
      # on pourrait faire une propagation d'erreur pour un except à l'extérieur de la fonction 
      # raise sqlite3.OperationalError(str(oe))
      return False, oe

if __name__ == "__main__":
  try:
    with sqlite3.connect("../dns.db") as conn:
      ret = execute_script("./domain_names_sqlite3.sql", conn)
      print(ret)
  except FileNotFoundError as fe:
    print(fe)
# %%
######## insertion de données en table 
"""
1. créer une liste de 100000 listes [nom de domaine, iso2] depuis le fichier dns_100000.csv
2. insérer en base avec la construction de la requête suivante:
   INSERT INTO (name, iso2) VALUES ('aaaaa.fr', 'FR'), ('bbbbb.fr', 'DE'), ... * 100000
hint: la méthode "???".join(???)
"""

from pathlib import Path
import pandas as pd
import csv
import sqlite3
 
csv_path = Path("..") / "data" / "dns_100000.csv"
dns_df = pd.read_csv(
  csv_path,
  sep=";",
  # simplifier le jeu d'entrée en développement
  # nrows=10,
  encoding="utf-8",
  usecols=["Nom de domaine", "Pays BE"]
)
dns_df

inserts = dns_df.values.tolist()
inserts
prepared = inserts.copy()
# with open(csv_path, mode="r", encoding="utf-8") as f:
#   rd = csv.reader(f, delimiter=";")
#   inserts = []
#   for line in rd:
#     inserts.append(line[:2])
# inserts

for i in range(len(inserts)):
  inserts[i] = "', '".join(inserts[i])
inserts

try:
  with sqlite3.connect("../dns.db") as conn:
    cur =  conn.cursor()
    # métaprogrammation: écriture d'une requête d'un langage de programmation à partir d'un autre
    # 1 requête avec 100000 lignes
    # req = f"INSERT INTO domain_name (name, iso2) VALUES ('{"'), ('".join(inserts)}')"
    # cur.execute(req)
    
    # VS requête préparée: 100000 requête avec 1 ligne par requête
    req = "insert into domain_name (name, iso2) values (?, ?)"
    cur.executemany(req, prepared)
    
    print(f"{cur.rowcount} éléments insérés")
except sqlite3.OperationalError as oe:
  print(oe)


# %%
