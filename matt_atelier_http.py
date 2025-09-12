# %%
########### téléchargement d'un document via http et requests
import requests
from pathlib import Path
# requests utilise urllib3
from urllib3.exceptions import HTTPError

URL = "https://www.afnic.fr/wp-media/ftp/documentsOpenData/202507_OPENDATA_D-NbDeNomsDeDomainesParCodePostalDuPointFr.zip"

data_dir = Path("..") / "data"

try:
  response = requests.get(URL)
except (requests.ConnectionError, HTTPError) as e:
  print(e)
else:
  if response.status_code == 200:
    if "Content-Type" in response.headers:
      # ici application/zip (archive à télécharger => en binaire)
      if "application/zip"  == response.headers["Content-Type"]:
        ## type de corps de la réponse
        # content = binaire
        with open(data_dir / "small_zip.zip", mode="wb") as f:
          f.write(response.content)

        ## text + encoding
        # response.text, response.encoding
        ## JSON
        # response.json()
# %%
###### EXERCICE API REST
"""
client vers https://gorest.co.in
1. écrire une classe GoRestClient attributs attendus 
   - le nom de domaine
   - la version
2. concentrer l'utilisation de requests dans une méthode privée __call
qui doit gérer tous les types de requêtes (GET, POST, PUT)
Hint: utiliser la fonction getattr
3. ajouter une méthode publique get_users qui va accumuler les résultats
   des appels à l'endpoint https://gorest.co.in/public/v2/users à pagigner
   jusqu'on ait tous les utilisateurs
"""
# %%
###### les fonctions getattr et setattr hasattr

class Truc:
  pass

tr = Truc()
# création dynamique d'un attribut à partir d'une str
setattr(tr, "param", 10)

tr.param
# retourner la valeur d'un attribut via une str
getattr(tr, "param")
hasattr(tr, "param")

nom = "joe"
# getattr(nom, "upper") est un attribut de type fonction/méthode
getattr(nom, "upper")()
# %%
