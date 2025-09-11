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
