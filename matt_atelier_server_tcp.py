######## socket client et serveur tcp
# le socket serveur tcp: la gestion des requêtes clientes va être exécuté dans un thread
from socket import *
from threading import Thread

PORT = 25029
# -----------------------------------------------------------------------------
# créer la socket serveur et écoute un port
# -----------------------------------------------------------------------------
def start_server():
  server = socket(AF_INET, SOCK_STREAM)
  # attacher la socket à une interface serveur et un port dispà
  server.bind(("127.0.0.1", 25029))
  # la socket ne peut accepter que jusqu'à 5 cnxs
  server.listen(5)
  return server

# -----------------------------------------------------------------------------
# gestion des requêtes clients
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
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