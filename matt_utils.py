DEFAULT = "N/A"

def parse_template(
    tpl: str, 
    data: dict, 
    delims: tuple=("{{", "}}"), 
    default: str=DEFAULT,
    **opts
  ) -> str:
  """
  interprète un template avec des données
  options **:
  debug=True
  ...
  """
  while tpl.find(delims[0]) != -1:
    start_index = tpl.index(delims[0]) + len(delims[0])
    end_index = tpl.index(delims[1])
    key = tpl[start_index:end_index]
    if "debug" in opts and opts["debug"]:
      print(f"DEBUG: key: {key}")
    tpl = tpl.replace(delims[0] + key + delims[1], data.get(key, default))
  return tpl