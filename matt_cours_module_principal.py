##### PROGRAMME PRINCIPAL
# %%
##### import avec espace de nom

# le fichier matt_utils.py est importable car dans le même dossier
# ~ chemin relatif
import matt_utils

# matt_utils est une variable module == espace de nom
matt_utils.parse_template("animal: {{pet}}", {"pet": "lapin"})

# %%
##### idem sans espace de nom
from matt_utils import parse_template
# from matt_utils import parse_template, DEFAULT
# from matt_utils import *

## REM: importer un module avec import ou from 
## ne fait que exécuter la totalité du code du module importé

parse_template("animal: {{pet}}", {"pet": "lapin"})

# %%
##### interêt de l'espace de nom et aliasing
from matt_utils import parse_template as parse_tpl

# collision de nom
parse_template = True

parse_tpl("animal: {{pet}}", {"pet": "lapin"})

# %%
