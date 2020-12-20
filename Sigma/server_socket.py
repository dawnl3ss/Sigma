import socket
import time

print("//~~ Server Side ~~//")

host, port = ("127.0.0.1", 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((host, port))
sock.listen(1)

(client, (host, port)) = sock.accept()

print("[+] Client connexion : {} with {}".format(host, port))

connect_accept = True

while connect_accept:
    command = input("\033[37m" + "root@server ~# ")
    
    if "exit" in command:
        client.sendall(command.encode())
        time.sleep(2)
        client.close()
        sock.close()
        connect_accept = False
    else:
        client.sendall(command.encode())
        result = client.recv(1024)
        print("\033[32m" + result.decode())

client.close()
sock.close()