def debug(key, var):
  """
  fonction générique à injecter
  dans des fonctions métier
  enrichit le debug
  """
  return f"DEBUG: {key}: {var}"