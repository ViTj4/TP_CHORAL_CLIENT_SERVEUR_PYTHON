import socket

# Adresse et port du serveur
server_address = ('localhost', 10000)

# Connexion au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Réception de la liste des chanteurs disponibles
available_chorale = eval(client_socket.recv(1024).decode('utf-8'))
print("Chanteurs disponibles :", available_chorale)

# Demande à l'utilisateur l'ordre de passage choisi
order = input("Entrez l'ordre de passage des chanteurs (par exemple, '012012') : ")
while len(order) < 6:
    print("L'ordre de passage doit comporter au moins 6 caractères.")
    order = input("Entrez l'ordre de passage des chanteurs (par exemple, '012012') : ")
client_socket.sendall(bytes(order, 'utf-8'))

# Boucle principale du client
while True:
    # Réception d'un message du serveur
    message = client_socket.recv(1024).decode('utf-8')

    # Affichage du message
    print(message)

    # Attente d'une nouvelle entrée utilisateur pour continuer
    input("Appuyez sur Entrée pour continuer...")
