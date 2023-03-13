import socket

# Création du socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Adresse et port du serveur
server_address = ('localhost', 10000)
server_socket.bind(server_address)

# Nombre maximal de clients connectés simultanément
MAX_CLIENTS = 5

# Liste des chanteurs disponibles
CHORALE = ['A', 'B', 'C']


# Fonction pour gérer une connexion client
def handle_client(client_socket):
    # Envoi de la liste des chanteurs disponibles
    client_socket.sendall(bytes(str(CHORALE), 'utf-8'))

    # Réception de l'ordre de passage choisi par le client
    order = client_socket.recv(1024).decode('utf-8')

    # Boucle principale du traitement
    current_chorale = ''
    current_triangle = 0
    for i in range(len(order)):
        if current_triangle == 3:
            client_socket.sendall(bytes("TRIANGLE", 'utf-8'))
            current_triangle = 0
        current_chorale = CHORALE[int(order[i])]
        client_socket.sendall(bytes(current_chorale, 'utf-8'))
        current_triangle += 1

    # Fermeture de la connexion client
    client_socket.close()


# Boucle principale du serveur
server_socket.listen(MAX_CLIENTS)
print("Serveur en attente de connexions...")
while True:
    # Attente d'une connexion client
    client_socket, client_address = server_socket.accept()
    print(f"Connexion reçue de {client_address}")

    # Traitement de la connexion dans un thread séparé
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
