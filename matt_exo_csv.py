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

parent_dir = Path("..")
big_zip = parent_dir / "202503_OPENDATA_A-NomsDeDomaineEnPointFr.zip"
data_dir = parent_dir / "data"

# mkdir -p en python
os.makedirs(data_dir, exist_ok=True)

# if not os.path.exists(data_dir / "dns.csv"):
if not (data_dir / "dns.csv").exists():
  with ZipFile(big_zip, mode="r") as zf:
    items = zf.namelist()
    zf.extract(items[0], path=data_dir)
    os.rename(data_dir / items[0], data_dir / "dns.csv")

# %%
