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

import requests
from urllib3.exceptions import HTTPError

class GoRestClient:
  def __init__(self, domain="gorest.co.in", version="v2"):
    self.__domain = domain
    self.__version = version
  
  def __call(self, method, endpoint):
    try:
      url = f"https://{self.__domain}/public/{self.__version}/{endpoint}"
      if not method in ("GET", "POST", "PUT", "DELETE"):
        raise ValueError(f"{method}: méthode non autorisée")
      response = getattr(requests, method.lower())(url)
      
      if response.status_code in (200,):
        if "content-type" in response.headers:
          if "application/json" in response.headers["content-type"]:
            data = response.json()
      else:
        data = response.json()
    except (requests.ConnectionError, HTTPError, ValueError) as e:
      data = {"message": str(e)}
    return data
        

  def get_users(self):
    # TODO : comment faire itérer les pages ?
    users = self.__call("GET", "users")
    return users

api = GoRestClient()
api.get_users()
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
