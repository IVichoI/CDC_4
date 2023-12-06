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
# message = 'localhost'
# stream_socket.sendall(message.encode('utf-8'))
while True:
  message = input("Ingrese un mensaje ('exit para salir'): ")

  # En cado de 'exit'
  if message == 'exit':
    stream_socket.sendall(message.encode('utf-8'))
    break

  # Enviar mensaje a Servidor
  stream_socket.sendall(message.encode('utf-8'))

  # Respuesta de servidor
  data = stream_socket.recv(40)
  print(f"Respuesta: {data.decode('utf-8')}")

# Obtiene las respuestas del servidos
# data = stream_socket.recv(16)
# print(data)

print('socket cerrado')
stream_socket.close()