from .text_cleaner import Cleaner

class Counter:
  def __init__(self, cleaner: Cleaner):
    # Injection de dependance => la classe counter ne connait que l'interface publique du cleaner
    # couplage faible entre les 2 classes
    self.__text = cleaner.clean()
  
  def count(self):
    occurences = {}
    for word in self.__text.split():
      if word in occurences:
        occurences[word] += 1
      else:
        occurences[word] = 1
    
    # changer le dictionnaire en une liste de tuples => occurences.items()
    # pour trier la liste selon l'occurence (valeur d'indice 1 du tuple)
    # en ordre décroissant
    # on affiche les 5 premiers éléments
    # on reconvertit la liste de tuples en un dictionnaire
    return dict(sorted(
      occurences.items(), 
      key=lambda tup: tup[1], 
      reverse=True
    )[:5])
