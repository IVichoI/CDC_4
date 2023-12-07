import socket
import time

if __name__ == "__main__":
  # Creación del socket UDP
  sock_b = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  # Dirección del servidor B
  server_address = ('localhost', 10000)

  # Enlazar el socket al puerto
  sock_b.bind(server_address)

  while True:
    print('\nEsperando solicitud de archivo...')
    data, address = sock_b.recvfrom(4096)
    # Data = solicitud ("Solicitar Datos")
    # Address = IP + port

    if data == b'Solicitar Datos':
      print('Solicitud de archivo aceptada.')
      sock_b.sendto(b'Positiva', address)

      # cola = threading.Thread(target=Peticiones)
      # Esperar a que se libere el archivo
      print('Esperando a que se libere el archivo...')
      # cola.start()
      data = 'void'
      while True:
        while data == 'void':
          data, address = sock_b.recvfrom(4096)
          time.sleep(1)

        if data == b'Archivo disponible':
          # with status.get_lock():
          #   status.value = 1
          print('Archivo liberado. Listo para nuevas solicitudes.')
          break

        elif data == b'Solicitar Datos':
          sock_b.sendto(b'Ocupado', address)
          data = 'void'


  sock_b.close()