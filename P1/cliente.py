import socket

if __name__ == "__main__":

  # Creacion del socket TCP
  stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  host = 'localhost'
  port = 5555

  server_address = ((host, port))

  print("Conectando...")
  stream_socket.connect(server_address)

  # Respuesta del Server
  data = stream_socket.recv(40)
  print(f"\nSERVIDOR: {data.decode('utf-8')}")


  print("\n\t¿Qué desea solicitar al servidor?\n")
  print("1. Inscribirse")
  print("2. Obtener fecha y hora del curso")
  print("3. Obtener posición de inscripción")
  print("4. Salir")

  while True:
    choice = input("\nEscoja una opcion: ")

    # Para el resto de opciones hay operaciones varias
    if choice == '1':
      stream_socket.sendall('inscripcion'.encode('utf-8'))
      data = stream_socket.recv(80)
      print(f"\nSERVIDOR: {data.decode('utf-8')}")

    elif choice == '2':
      stream_socket.sendall('fecha'.encode('utf-8'))
      data = stream_socket.recv(56)
      print(f"SERVIDOR: {data.decode('utf-8')}")

    elif choice == '3':
      stream_socket.sendall('posicion'.encode('utf-8'))
      data = stream_socket.recv(50)
      print(f"SERVIDOR: {data.decode('utf-8')}")

    elif choice == '4':
      stream_socket.sendall('exit'.encode('utf-8'))
      break

  print('\nSocket cerrado')
  stream_socket.close()