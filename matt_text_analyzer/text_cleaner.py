import re
import string

class Cleaner:
  def __init__(self, text: str):
    self.__text = text
  
  def __clean_punctuation(self):
    self.__text = re.sub(f"[{string.punctuation}]", " ", self.__text)

  def __clean_breaks(self):
    # raw string: qui traite le \ comme \
    self.__text = re.sub(r"\r?\n", " ", self.__text)
  
  def __clean_spaces(self):
    self.__text = re.sub(" +", " ", self.__text)
  
  def __remove_little_words(self):
    words = []
    for word in self.__text.split():
      if len(word) > 3:
        words.append(word)
    self.__text = " ".join(words)

  def clean(self) -> str:
    self.__clean_punctuation()
    self.__clean_breaks()
    self.__clean_spaces()
    self.__remove_little_words()
    return self.__text