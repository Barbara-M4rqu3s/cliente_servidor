import threading
import socket

# Lista para armazenar clientes.
clients = []

input("digite a porta: ")
input("digite o endereço: ")

def main():
    # IPv4 e protocolo TCP.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Tentar ligar o servidor.
    try:
        server.bind(("localhost", 7777))
        server.listen()
    except:
        return print("\nNão foi possível iniciar o servidor!\n")
    
    # Loop para aceitar conexões.
    while True:
        client, addr = server.accept()
        
        # Adicionar clientes na lista clients.
        clients.append(client)
        
        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start() 
         
# Tratamento de mensagens.       
def messagesTreatment(client):
    while True:
        # Tentar enviar as mensagens aos usuários.
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break
        
# Verificar o cliente que mandou a mensagem,
# para não reenviar a mensgem desnecessariamente.
def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            # Tentar enviar mensagem ao usuário
            try:
                clientItem.send(msg)
            # Caso o servidor não consiga se comunicar com o cliente,
            # o usuário será deletado.
            except:
                deleteClient(clientItem)
#                 
def deleteClient(client):
    clients.remove(client)
    
main()
    
    
    
    