# %%
############### client socket tcp
from socket import socket, AF_INET, SOCK_STREAM, gaierror

# on va demander les robots.txt
URL = 'www.wellho.net'

# socket réseau(AF_INET) & tcp (SOCK_STREAM)
sock = socket(AF_INET, SOCK_STREAM)

try:
  # socket = combinaison url + port
  sock.connect((URL, 80))
# gai : getaddrinfo()
except gaierror as e:
  print(f"unable to connect to {URL}: {e}")

req = f"GET /robots.txt HTTP/1.1\r\nHost: {URL}\r\n\r\n"
# envoie la requête TCP sous forme d'octets
# retourne le nb d'octets envoyés qui peut être < total
sock.send(bytes(req, "utf-8"))

## attendre la réponse
while True:
  # réception de la réponse par lots
  data = sock.recv(2048)
  if data == b'': break
  # affichage en utf-8
  print(data.decode("utf-8"))

# fermer une socket
sock.close()

# %%
######## socket client et serveur tcp
# le socket serveur tcp: la gestion des requêtes clientes va être exécuté dans un thread
from socket import *
from threading import Thread

PORT = 25029

# créer la socket serveur et écoute un port
def start_server():
  server = socket(AF_INET, SOCK_STREAM)
  # attacher la socket à une interface serveur et un port dispà
  server.bind(("127.0.0.1", 25029))
  # la socket ne peut accepter que jusqu'à 5 cnxs
  server.listen(5)
  return server

## gestion des requêtes clientes
def accept_server(server: socket):
  # accept attend une requête 
  # et retourne socket client pour la réponse et l'addresse du client
  try:
    conn, addr = server.accept()
    with conn:
      while True:
        data = conn.recv(1024)
        if data == b'quit':
          break
        if data != b'':
          _str = data.decode("utf-8")
          print(f"server: {_str}")
        # send reprise en cas d'erreur
        conn.sendall(bytes(_str[::-1], "utf-8"))
  except ConnectionAbortedError as e:
    print(e)

if __name__ == "__main__":
  # mise en place du serveur
  server = start_server()

  thread = Thread(target=accept_server, args=(server,))
  thread.start()
  
  #### client
  with socket(AF_INET, SOCK_STREAM) as sock:
    sock.connect(('127.0.0.1', PORT))
    sock.send(b'some data to process\nEND')
    data = sock.recv(1024)
    print(f"client: {data.decode("utf-8")}")
    thread.join(2)
    server.close()

# %%
