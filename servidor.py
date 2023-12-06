import socket
import sys

# Creacion del socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definicion del servidor
host = 'localhost'

# Definicion del puerto de comunicacion
# Especifica el puerto con el que nos queremos comunicar
port = 5555

# Vincular con el socket al puerto
sock.bind((host, port))

# Escuchando las conexiones entrantes
sock.listen(1)

# Esperando por conexion
print("Esperando una conexion")
connection, client = sock.accept()

print(client, 'conectado..')

# Recibir los datos en pequeños fragmentos y retransmitirlos

data = connection.recv(16)
print('recivido %s"' %data)

if data:
  connection.sendall(data)
else:
  print('Sin mensaje', client)

# Cerrar la conexion
connection.close()