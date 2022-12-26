import threading
import socket

def main():
    
    # IPv4 e protocolo TCP.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Tentar conectar-se ao ao servidor.
    try:
        client.connect(("localhost", 7777))
        
    # Se não houver conexão com o servidor, o usuário será notificado.
    except: 
        return print("\n Não foi possivel se conectar ao servidor!\n")
    
    # Nome do usuário.
    user = input("Usuário> ")
    print("\nConectado.")

    # Funções para rodar o envio e o recebimento de mensagens simultaneamente. 
    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, user])
 
    # Execução das funções.
    thread1.start()
    thread2.start()
    
# Receber mensagens.    
def receiveMessages(client):
    while True:
        try:
            # Transformar bytes em strings.
            msg = client.recv(2048).decode("utf-8")
            print(msg + "\n")
        except:
            print("\nNão foi possivel permanecer conectado no servidor!\n")
            print("Pressione <Enter> Para continuar...")
            client.close()
            break
        
# Enviar mensagens.
def sendMessages(client, user):
    while True:
        try:
            msg = input("\n")
            client.send(f"<{user}> {msg}".encode("utf-8"))
        except:
            return

main()
