import socket
import sys

# Creacion del socket TCP
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definicion del servidor
host = 'localhost'

# Definicion del puerto de comunicacion
# Especifica el puerto con el que nos queremos comunicar
port = 5555

# Conectando el socket al puerto donde el server esta escuchando
server_address = ((host, port))

print("Conectando...")

stream_socket.connect(server_address)

# Envia solicitud de datos al servidor
message = 'Hola Server Perron'
stream_socket.sendall(message.encode('utf-8'))

# Obtiene las respuestas del servidos
data = stream_socket.recv(10)
print(data)

print('socket cerrado')
stream_socket.close()