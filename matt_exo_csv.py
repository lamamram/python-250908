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