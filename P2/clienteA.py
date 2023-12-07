import socket
import time

# Creación del socket UDP
sock_a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Dirección del servidor B
server_address = ('localhost', 10000)

choice = 'Y'
while choice == 'Y':

  # Enviar solicitud de archivo al servidor B
  file_request = b'Solicitar Datos'
  sock_a.sendto(file_request, server_address)

  # Recibir respuesta del servidor B
  data, address = sock_a.recvfrom(4096)
  response = data.decode('utf-8')

  if response == 'Positiva':
    print('Respuesta positiva recibida de B. Usando el archivo...')
    time.sleep(10) # Simulación del uso del archivo

    print('Archivo utilizado. Liberando archivo...')
    sock_a.sendto(b'Archivo disponible', server_address)

  elif response == 'Ocupado':
    print('El archivo está siendo ocupado por otro usuario, intentelo más tarde.')

  else:
    print('\nHa ocurrido un error inesperado')
  
  choice = input("\n¿Quiere intentar solicitar el archivo nuevamente? (Y/n): ")

sock_a.close()
