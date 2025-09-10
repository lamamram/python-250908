import re
import string

class Cleaner:
  def __init__(self, text: str):
    self.__text = text
  
  def __clean_punctuation(self):
    self.__text = re.sub(f"[{string.punctuation}]", " ", self.__text)

  def clean(self) -> str:
    self.__clean_punctuation()
    return self.__text