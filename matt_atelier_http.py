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
