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
4. lancer plusieurs pages à la fois en utilisant la classe concurrent.futures.ThreadPoolExecutor
   REM: on ne peut faire de multithreading en python qu'avec les I/O non avec le CPU 
   à cause du GIL (Global Interpretator Lock)
"""

import requests
from urllib3.exceptions import HTTPError
from dotenv import load_dotenv
import os
from concurrent.futures import ThreadPoolExecutor as TPE
from multiprocessing import cpu_count

## gestion des variables d'environnement
## pip install python_dotenv
# avec un fichier .env à la racine API_TOKEN=......
# load_dotenv charge les variables du .env en tant que envvar
load_dotenv()


class GoRestClient:
  def __init__(self, domain="gorest.co.in", version="v2"):
    self.__domain = domain
    self.__version = version
    self.__token = os.environ["API_TOKEN"]
  
  def __call(self, method, endpoint, *, body={}, headers={}):
    try:
      url = f"https://{self.__domain}/public/{self.__version}/{endpoint}"
      if not method in ("GET", "POST", "PUT", "DELETE"):
        raise ValueError(f"{method}: méthode non autorisée")
      # simple authentification avec token
      if method in ("POST", "PUT"):
        headers["Authorization"] = f"Bearer {self.__token}"
      response = getattr(requests, method.lower())(url, data=body, headers=headers)
      
      # 200 ok pour GET et 201 ok pour POST
      if response.status_code in (200, 201):
        if "content-type" in response.headers:
          if "application/json" in response.headers["content-type"]:
            data = response.json()
      else:
        raise ValueError(f"{response.status_code}: {response.text}")
    except (requests.ConnectionError, HTTPError, ValueError) as e:
      data = {"message": f"{e} {type(e)}"}
    return data
        
  def get_users(self):
    users, i = [], 1
    while True:
      data = self.__call("GET", f"users?page={i}&per_page=100")
      print(f"page {i} fetched !")
      # erreur
      if isinstance(data, dict): return data
      # plus de donnée
      if not data: break
      users += data
      i += 1   
    return users
  
  def create_user(self, user: dict):
    return self.__call("POST", "users", body=user)


  ################ MULTITHREADING ###################
  
  # worker
  def get_page(self, page_id):
    print(f"page {page_id} fetched !")
    return self.__call("GET", f"users?page={page_id}&per_page=100")

  def get_users_multi(self, nb_workers=cpu_count()//2):
    data = []
    i = 0
    with TPE(max_workers=nb_workers) as pool:
      # lancement synchrone de workers => map bloque le programme tant que les workers
      # son terminés
      while True:
        start_index, end_index = i * nb_workers + 1, (i + 1) * nb_workers + 1
        # la pool exécute nb_workers * self.get_page en // avec les nb_workers * page_id
        responses = pool.map(self.get_page, list(range(start_index, end_index)))
        for response in responses:
          if not response: return data
          data += response
        i += 1
    return data

api = GoRestClient()
# api.get_users()

user = {
    "name": "LAMAM",
    "email": "admin2@example.com",
    "gender": "male",
    "status": "active"
}

# api.create_user(user)
api.get_users_multi()

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
