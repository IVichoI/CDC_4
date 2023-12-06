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
# data = connection.recv(16)
# print('\nrecivido %s"' %data)

try:
  # Esperar por una conexión
  print("Cliente conectado.")
  try:
    while True:
      # Recibir datos en pequeños fragmentos y retransmitirlos
      data = connection.recv(16)
      if data.decode('utf-8') == 'exit':
        break  # Salir del bucle si no hay datos
      print(f"Mensaje recibido: {data.decode('utf-8')}")

      # Enviar una respuesta al cliente
      message = f"Mensaje recibido por el servidor: {data.decode('utf-8')}"
      connection.sendall(message.encode('utf-8'))
  finally:
    # Cerrar la conexión con el cliente
    print("Fin")
except KeyboardInterrupt:
  print("Servidor interrumpido por el usuario.")
finally:
# if data:
#   connection.sendall(data)
# else:
#   print('Sin mensaje', client)

# Cerrar la conexion
  connection.close()