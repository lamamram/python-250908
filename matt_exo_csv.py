"""
URL: https://www.afnic.fr/wp-media/ftp/documentsOpenData/202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip

1. télécharger via un navigateur

BONUS
1bis.téléchargement en GET et en binaire
outils: pip install requests

2. extraire le fichier .csv contenu dans le zip à télécharger
hint: zipfile.Zipfile (doc ou google/stackoverflow)
hint: les zip s'ouvrent et se ferment

3. renommer le fichier csv en dns.csv 
   dans un dossier "data" dûment créé dans le dossier parent

4. ne faire ce qui précède que si ce n'est pas déjà fait

5. écrire un script qui
- extrait n=2 paquets de nb_line=100000 lignes de donnée, sans le header
- appelle une fonction qui
   - créé un nouveau fichier csv à nommer en fct du nb de ligne
   - insère le header dans ce nouveau fichier
   - écrit le paquet de lignes

modus operandi: faire ceci en n'ouvrant le csv en lecture qu'une seule fois
"""

# %%
from pathlib import Path

# gestion auto de l'os
current = Path(".")
## diférentes propriétés intéressante
# relatif <=> absolu
# aller vers la gauche
# sortir les chemins en str
str(current.absolute().parent)
parent_dir = current.absolute().parent
# opérateur / permet de créer des chemins dynamiques
current_dir = parent_dir / "formation_python"
current_dir
# %%
from pathlib import Path
import os
from zipfile import ZipFile
import csv

parent_dir = Path("..")
big_zip = parent_dir / "202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
data_dir = parent_dir / "data"
new_name = "dns.csv"
nb_lines = 100000
nb_slices = 2

def write_csv(path):
  with open(
  path, 
  mode="w", 
  encoding="utf-8",
  newline=""
) as f:
    writer = csv.writer(f, delimiter=";", quotechar='"')
    writer.writerow(header)
    writer.writerows(rows)
    # ne fonctionne pas car rows devient locale
    # rows = []
    # fonctionne car mutable
    rows.clear()

# mkdir -p en python
os.makedirs(data_dir, exist_ok=True)

# if not os.path.exists(data_dir / "dns.csv"):
if not (data_dir / new_name).exists():
  with ZipFile(big_zip, mode="r") as zf:
    items = zf.namelist()
    zf.extract(items[0], path=data_dir)
    os.rename(data_dir / items[0], data_dir / new_name)

with open(
  data_dir / new_name, 
  mode="r", 
  encoding="utf-8",
) as f:
  reader = csv.reader(f, delimiter=";")
  header = next(reader)
  rows = []
  # itérer également sur les n° de lignes qui commencent à 1
  for i, row in enumerate(reader, start=1):
    if i > nb_lines * nb_slices: break
    rows.append(row)
    # tant qu'on ait pas à 100000 , 200000, (un mutltiple de 100000)
    if i % nb_lines: continue
    write_csv(data_dir / f"dns_{i}.csv")
    # rows = []

# %%
